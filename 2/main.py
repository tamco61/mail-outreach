import sys
import requests


def get_text(filename):
    with open(filename, encoding="utf-8") as f:
        text = f.read().strip()
    return text


def get_chats(token):
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url)
    result = response.json()["result"]

    chats = {}
    for update in result:
        chat = update["message"]["chat"]
        chat_id = chat["id"]
        if chat_id not in chats:
            if "title" in chat:
                title = chat["title"]
            else:
                title = chat["username"]
            chats[chat_id] = title

    return chats


def send_message(token, message, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML'
    }

    response = requests.post(url, data=payload)


def main():
    if len(sys.argv) == 3:
        token_filename, message_filename = sys.argv[1:]

        token = get_text(token_filename)
        message = get_text(message_filename)
        chats = get_chats(token)

        print("Доступные чаты:")
        print("id\t\ttitle")
        for chat_id, title in chats.items():
            print(chat_id, title, sep="\t")
        print("Выберите доступный чат (в качестве выбора отправьте наберите его id):")
        chat_id = int(input())

    elif len(sys.argv) == 4:
        token_filename, message_filename, chat_id = sys.argv[1:]

        token = get_text(token_filename)
        message = get_text(message_filename)
        chat_id = int(chat_id)
    else:
        print("неверный формат ввода")
        sys.exit(1)

    send_message(token, message, chat_id)


if __name__ == "__main__":
    main()