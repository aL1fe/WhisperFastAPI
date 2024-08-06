# Используем официальный базовый образ с поддержкой CUDA
FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu20.04

# Обновляем список пакетов
RUN apt-get update

# Устанавливаем утилиту для настройки временной зоны
RUN apt-get install -y tzdata

# Настраиваем временную зону
RUN ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime \
    && dpkg-reconfigure --frontend noninteractive tzdata

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    sudo \
    python3.9 \
    python3-distutils \
    python3-pip \
	python3-dev \
    ffmpeg

# Устанавливаем pip и необходимые библиотеки Python
RUN pip3 install --upgrade pip
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117

# Устанавливаем библиотеку для работы с Whisper
RUN pip3 install openai-whisper

# Скачиваем модель
RUN whisper --model large-v3

# Устанавливаем дополнительные зависимости (если необходимо)
RUN pip3 install numpy scipy

# Копируем скрипты и файлы проекта в контейнер
COPY . /app
WORKDIR /app

# Указываем команду для запуска приложения
CMD ["python3", "your_script.py"]
