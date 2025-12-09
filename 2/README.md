# Установка библиотек
```(bash)
pip install -r requirement.txt
```  

# Запуск в случае, когда id чата известно
```(bash)
python .\main.py <token-file-path> <message-file-path> <chat-id>
```  
**token-file-path** файл с токеном бота  
**message-file-path** файл с текстом сообщения  
**chat-id** id чата куда нужно отправить сообщение

# Запуск в случае, когда id чата неизвестно
```(bash)
python .\main.py <token-file-path> <message-file-path>
```  
**token-file-path** файл с токеном бота  
**message-file-path** файл с текстом сообщения
