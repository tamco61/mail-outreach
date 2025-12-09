# Установка библиотек
```(bash)
pip install -r requirement.txt
```  

# Запуск
```(bash)
python .\main.py .\email.txt
```  
# Пример email.txt
test@gmail.com  
noreply@yandex.ru  
user@nesushchestvuet12345.com  
info@internal.company.local  
any@mail.box  
any@habr.com  

# Пример вывода
test@gmail.com  домен валиден  
noreply@yandex.ru       домен валиден  
user@nesushchestvuet12345.com   домен отсутствует  
info@internal.company.local     MX-записи отсутствуют или некорректны  
any@mail.box    домен отсутствует  
any@habr.com    домен валиден  
