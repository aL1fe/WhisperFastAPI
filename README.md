How to first run on local PS.
0.	Download ffmpeg.exe and put it in folder with main.py.
1.	Open Power Shell in folder with main.py.
2.	Use command to start configuration and set up virtual environment: .\startup.ps1
	Wait until you will see the next one: (venvMS) PS D:\Alex\Programming\MeetingSummarizer>
	Also folders __pycache__ and venvMS will be genereted.
3.	Use command to run the application: uvicorn main:app --host 127.0.0.1 --port 8005
	Wait for you will see:
	INFO:     Started server process [19792]
	INFO:     Waiting for application startup
	INFO:     Application startup complete
	INFO:     Uvicorn running on http://127.0.0.1:8005 (Press CTRL+C to quit)
4.	Open brouser: http://127.0.0.1:8005/docs
	You will see swagger.

<!--
1.	Open Power Shell in folder with main.py.
2.	Use command to run the application: .\run.ps1
	Wait for you will see:
	INFO:     Started server process [19792]
	INFO:     Waiting for application startup
	INFO:     Application startup complete
	INFO:     Uvicorn running on http://127.0.0.1:8005 (Press CTRL+C to quit)
3.	Open brouser: http://127.0.0.1:8005/docs
	You will see swagger.
--> 