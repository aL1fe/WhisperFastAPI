Requirements
1. Check if Python is Installed
	1.1. Open PowerShell.
	1.2. Run the following command:
		python --version
2. Check if CUDA is Installed
	2.1. Open PowerShell.
	2.2. Run the following command:
		nvidia-smi
	2.3. Make sure that you see CUDA version
-------------------------------------------------------------------------------------------
How to first run on the local PS.
1.	Download ffmpeg.exe and put it in folder with main.py.
2.	Open Power Shell in folder with main.py.
3.	Use command to start configuration and set up virtual environment: .\startup.ps1
	Wait until you will see the next one: (.venv) PS D:\Alex\Programming\MeetingSummarizer>
	Folders .venv and __pycache__ will be genereted.
4.	Wait for you will see:
	INFO:     Started server process [19792]
	INFO:     Waiting for application startup
	INFO:     Application startup complete
	INFO:     Uvicorn running on http://0.0.0.0:8005 (Press CTRL+C to quit)
5.	Open brouser: http://127.0.0.1:8005/docs
	You will see Swagger.

The second and subsequent runs on the local PS.
1.	Open Power Shell in folder with main.py.
2.	Use command to run the application: .\run.ps1
	Wait for you will see:
	INFO:     Started server process [19792]
	INFO:     Waiting for application startup
	INFO:     Application startup complete
	INFO:     Uvicorn running on http://0.0.0.0:8005 (Press CTRL+C to quit)
3.	Open brouser: http://127.0.0.1:8005/docs
	You will see swagger.
-------------------------------------------------------------------------------------------
Possible errors.
Traceback (most recent call last):
  File "C:\meetingsummarizer\main.py", line 2, in <module>
    import torch
  File "C:\meetingsummarizer\.venv\Lib\site-packages\torch\__init__.py", line 148, in <module>
    raise err
OSError: [WinError 126] The specified module could not be found. Error loading "C:\meetingsummarizer\.venv\Lib\site-packages\torch\lib\fbgemm.dll" or one of its dependencies.

How to fix.
1. Download libomp140.x86_64.dll and put it to C:\Windows\System32
2. Install VC_redist.x64.exe if needed.
-------------------------------------------------------------------------------------------
Useful links.
OpenAI/whisper-large-v3 model
https://huggingface.co/openai/whisper-large-v3

How to install Pytorch with CUDA Version
https://www.gpu-mart.com/blog/Installing-pytorch-with-cuda-support-on-Windows

Torch Installation Command Generator
https://pytorch.org/get-started/locally/
