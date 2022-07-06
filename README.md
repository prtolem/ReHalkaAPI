# ReHalkaAPI
Это оболочка для апи сервиса решения капчи https://rehalka.online/
____
Примеры кода в синхронном режиме:
```python
from RehalkaApi import ReHalka

# инициализация апи
solver = ReHalka('token')
# отправка капчи на сервер
captcha_id = solver.send_captcha(domain='discord.com', site_key='site_key')
# получение ответа на капчу
captcha_answer = solver.get_captcha_answer(captcha_id=captcha_id)
```

____
Пример кода в асинхронном режиме:
```python
import asyncio

from RehalkaApi import AioReHalka


async def main():
    # инициализация апи
    solver = AioReHalka('token')
    # Создание сессии
    session = await AioReHalka.create_session()
    # отправка капчи на сервер
    captcha_id = await solver.send_captcha(session=session, domain='discord.com', site_key='site_key')
    # получение ответа на капчу
    captcha_answer = await solver.get_captcha_answer(session=session, captcha_id=captcha_id)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

```
___
Возможные ошибки от сервера:
- ERROR_KEY_DOES_NOT_EXIST = нет или неправильный ключ апи
- ERROR_ZERO_BALANCE = закончились деньги на балансе
- ERROR_NO_SLOT_AVAILABLE = нет свободных слотов, подождите и повторите запрос
- ERROR_CAPTCHA_UNSOLVABLE = сервис не смог решить капчу
- ERROR_WRONG_SAITKEY = Не верный ключ сайта
- ERROR_WRONG_CAPTCHA_ID = не верный айди капчи
- CAPCHA_NOT_READY = капча еще не готова
____
By Derk/Prtolem/Kiber

Contacts: 
https://t.me/derkown

Тема: https://zelenka.guru/threads/3585935
