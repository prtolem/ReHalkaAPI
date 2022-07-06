import asyncio

import aiohttp


class AioReHalka:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'http://185.189.167.221:3005'

    async def create_session(self):
        return aiohttp.ClientSession()
        # async with aiohttp.ClientSession() as session:
        #     return session

    async def send_captcha(self, session: aiohttp.ClientSession, domain: str, site_key: str) -> str:
        """
        IP_SERVER = 185.189.167.221:3005
        Отправить запрос с ключем и доменом от капчи
        http://{IP_SERVER}/in.php?userkey={api_key}&host={domain}&sitekey={site_key}
        :param session: Асинхронная сессия aiohttp
        :type session: aiohttp.ClientSession
        :param domain: Домен сайта на котором нужно решить капчу
        :type domain: str
        :param site_key: Ключ капчи
        :type site_key: str
        :return: В ответ получите {ID} капчи OK|1234567
        :rtype: str
        """
        async with session.get(
                self.base_url + f'/in.php?userkey={self.access_token}&host={domain}&sitekey={site_key}') as response:
            return await response.text()

    async def get_captcha_answer(self, session: aiohttp.ClientSession, captcha_id: str) -> str:
        """
        IP_SERVER = 185.189.167.221:3005
        Отправить запрос с номер решаемой капчи
        http://{IP_SERVER}/res.php?userkey={api_key}&id={captcha_id}
        :param session: Асинхронная сессия aiohttp
        :type session: aiohttp.ClientSession
        :param captcha_id: Айди капчи из метода send_captcha
        :type captcha_id: str
        :return: Когда капча решится сервер вернет ответ капчи OK|P0_eyJ0eXAiOiJKV......
        :rtype: str
        """
        async with session.get(self.base_url + f'/res.php?userkey={self.access_token}&id={captcha_id}') as response:
            return await response.text()
