# Вибираємо базовий образ Python
FROM python:3.9-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо requirements.txt в робочу директорію
COPY requirements.txt .

# Встановлюємо залежності
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Копіюємо весь код в робочу директорію
COPY . .

# Задаємо змінні середовища (можна задавати при запуску контейнера)

ENV API_ID=12345678
ENV API_HASH=12345678987654321234567890987654
ENV PHONE_NUMBER='+380XXXXXXXXX'
ENV SOURCE_CHANNEL_USERNAME='@dtek_svitlo_official'
ENV DESTINATION_CHAT_ID=-100000000000
ENV TEXT_PATTERN='3\s*груп[ау]'
ENV TIME_PATTERN='\b\d{2}:\d{2}\b'

# Команда, яка буде виконуватися при запуску контейнера
CMD ["python", "dtek_parser.py"]
