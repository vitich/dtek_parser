#!/usr/bin/env python3

from telethon import TelegramClient, events
import asyncio
import re
import json
import os

# Введіть тут ваші облікові дані з змінних середовища
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
source_channel_username = os.getenv('SOURCE_CHANNEL_USERNAME')
destination_chat_id = int(os.getenv('DESTINATION_CHAT_ID'))

# Отримуємо патерни з змінних середовища
text_pattern_str = os.getenv('TEXT_PATTERN')
time_pattern_str = os.getenv('TIME_PATTERN')

# Патерн для пошуку
text_pattern = re.compile(text_pattern_str, re.IGNORECASE)  # Ігнорує регістр
time_pattern = re.compile(time_pattern_str)  # Для пошуку часу у форматі ЧЧ:ММ

# Ініціалізація клієнта
session_name = '/app/session/session_name'
client = TelegramClient(session_name, api_id, api_hash)

# Тимчасовий файл для зберігання останнього повідомлення
last_message_file = '/app/session/last_message.json'

def load_last_message():
    if os.path.exists(last_message_file):
        with open(last_message_file, 'r') as f:
            return json.load(f)
    return {'message_id': None}

def save_last_message(message_id):
    with open(last_message_file, 'w') as f:
        json.dump({'message_id': message_id}, f)

def extract_relevant_lines(message_text):
    lines = message_text.split('\n')
    relevant_lines = []
    last_time = None

    for line in lines:
        cleaned_line = line.strip()
        if time_pattern.search(cleaned_line):
            last_time = time_pattern.search(cleaned_line).group()
        
        if text_pattern.search(cleaned_line):
            if last_time:
                relevant_lines.append(f"💡 О {last_time}\n{cleaned_line}")
            else:
                relevant_lines.append(f"{cleaned_line}")

    return relevant_lines

async def check_for_new_messages():
    try:
        async with client:
            source_channel = await client.get_entity(source_channel_username)
            last_message = load_last_message()

            async for message in client.iter_messages(source_channel, limit=1):
                if last_message and message.id == last_message['message_id']:
                    print(f"Повідомлення з id {message.id} вже оброблено.")
                    break

                print(f"Обробляю повідомлення з id {message.id}.")
                print(f"Текст повідомлення: {message.text}")  # Логування тексту повідомлення
                relevant_lines = extract_relevant_lines(message.text)
                if relevant_lines:
                    for line in relevant_lines:
                        print(f"Надсилаю: {line}")
                        await client.send_message(destination_chat_id, line)
                    save_last_message(message.id)  # Оновлюємо ID останнього обробленого повідомлення
                else:
                    print("Відповідних рядків не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

# Основний цикл
async def main():
    while True:
        await check_for_new_messages()
        await asyncio.sleep(60)  # Затримка в 60 секунд

if __name__ == '__main__':
    # Запускаємо сесію або авторизуємося, якщо сесії не існує
    with client:
        client.start(phone=lambda: phone_number)
        client.loop.run_until_complete(main())
