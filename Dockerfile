FROM al1fe/whisper_base

WORKDIR /app

COPY . .

CMD [ "python", "main.py" ]
