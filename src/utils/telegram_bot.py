import requests

TELEGRAM_TOKEN = '7818888018:AAGWXWTvlGV8YbqNYIInrVXd7CKeCXnmYYE'  # Replace with your actual bot token
CHAT_ID = '6551776615'  # Replace with your Telegram chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(url, data=payload)
    return response.status_code
