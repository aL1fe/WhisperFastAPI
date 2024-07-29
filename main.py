from fastapi import FastAPI, UploadFile
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import time
import os

if torch.cuda.is_available():
    device = "cuda:0"
    print("CUDA is available. Using GPU.")
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
    batch_size=16,
    # return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
    generate_kwargs={"language": "en", "suppress_tokens": []}  
)

app = FastAPI()    

@app.post("/upload/")
async def upload_file(file: UploadFile):
    with open(file.filename, "wb") as f:
        f.write(await file.read())
        
    startTime = time.time()

    result = pipe(file.filename)
    
    executionTime = round((time.time() - startTime), 2)
    
    os.remove(file.filename)    #Delete file after processing

    return {"TranscribedRecord": result["text"], "executionTime": f"{executionTime} sec"}

    
# If the script is executed as the main module, start the ASGI-server on the 8005 port
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)