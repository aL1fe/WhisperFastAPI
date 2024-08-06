python -m venv .venv
.\.venv\Scripts\activate.ps1
python -m pip install --upgrade pip
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r .\requirements.txt
python .\main.py
