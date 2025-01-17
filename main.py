from fastapi import FastAPI, UploadFile
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import time
import os
from dotenv import load_dotenv
from module_file import save_file
import asyncio
from typing import AsyncIterator


load_dotenv()
is_delete_after_processing = (os.getenv('WHISPER_IS_DELETE_AFTER_PROCESSING', 'False')
                              .lower() in ('true', '1', 'yes'))
upload_folder = 'incoming_files'

if torch.cuda.is_available():
    device = "cuda:0"
    print("CUDA is available. Using GPU.")
    print(f"Torch CUDA version {torch.version.cuda}")
else:
    device = "cpu"
    print("CUDA is not available. Using CPU.")

torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=25,
    batch_size=1,
    # return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
    generate_kwargs={"language": "en", "suppress_tokens": []}
)

app = FastAPI()


async def transcribe_file(file):
    file_path = await save_file(file, upload_folder)

    start_time = time.time()

    result = pipe(file_path)  # Transcribe file
    print(f"File {file.filename} was transcribed.")

    execution_time = round((time.time() - start_time), 2)

    # TODO save TranscribedRecord output_file_path = os.path.join(output_folder, f"{filename}.mp")

    if is_delete_after_processing:
        os.remove(file_path)  # Delete file after processing

    return result, execution_time


@app.post("/upload/")
async def upload_file(file: UploadFile):
    try:
        result, execution_time = await transcribe_file(file)
        return {"TranscribedRecord": result["text"], "executionTime": f"{execution_time} sec"}
    except Exception as e:
        return {"Error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)

# TODO add Rabbit<Q
