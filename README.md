Requirements
1. Check if Python is Installed
	1.1. Open PowerShell.
	1.2. Run the following command:
		python --version
2. Check if CUDA is Installed
	2.1. Open PowerShell.
	2.2. Run the following command:
		nvidia-smi

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


