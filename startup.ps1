python -m venv venvMeetSum
.\venvMeetSum\Scripts\activate.ps1
python -m pip install --upgrade pip
pip install --upgrade git+https://github.com/huggingface/transformers.git accelerate datasets[audio]
pip install -r requirements.txt
python .\main.py
# uvicorn main:app --host 127.0.0.1 --port 8005