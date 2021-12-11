# Обрезка ссылок с помощью Битли
Данный скрипт принимает url адрес и
создает из него короткую версию с помощью сервиса bitly.com.
В случае если скрипту передать уже созданный битлинк,
то скрипт отобразит количество переходов по этому битлинку

## Как установить
Вам необходимо зарегистрироваться на сайте bitly.com и получить API KEY, 
получить его можно после регистрации пройдя по данной ссылке:
https://bitly.com/a/sign_in?rd=/settings/api/
Полученный ключ вам необходимо прописать в файл .env таким образом:
API_BITLY_TOKEN=Ваш_API_KEY

Для работы скрипта вам понадобятся:
Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
'''html
pip install -r requirements.txt
'''
python-dotenv версии 0.19.2


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков bit.ly/3GQtQA3
