import sys
import requests


def get_text(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read().strip()
    return text


def send_message(token, message, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }

    response = requests.post(url, data=payload)


def main():
    if len(sys.argv) == 4:
        token_filename, message_filename, chat_id = sys.argv[1:]
        chat_id = int(chat_id)
        token = get_text(token_filename)
        message = get_text(message_filename)
        send_message(token, message, chat_id)


if __name__ == "__main__":
    main()