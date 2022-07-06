import requests


class ReHalka:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'http://185.189.167.221:3005'
        self.session = requests.Session()

    def send_captcha(self, domain, site_key) -> str:
        """
        IP_SERVER = 185.189.167.221:3005
        Отправить запрос с ключем и доменом от капчи
        http://{IP_SERVER}/in.php?userkey={api_key}&host={domain}&sitekey={site_key}
        :param domain: Домен сайта на котором нужно решить капчу
        :type domain: str
        :param site_key: Ключ капчи
        :type site_key: str
        :return: В ответ получите {ID} капчи OK|1234567
        :rtype: str
        """
        return self.session.get(
            self.base_url + f'/in.php?userkey={self.access_token}&host={[domain]}&sitekey={site_key}').text

    def get_captcha_answer(self, captcha_id) -> str:
        """
        Отправить запрос с номер решаемой капчи
        http://{IP_SERVER}/res.php?userkey={api_key}&id={captcha_id}
        :param captcha_id: Айди капчи из метода send_captcha
        :type captcha_id: str
        :return: Когда капча решится сервер вернет ответ капчи OK|P0_eyJ0eXAiOiJKV......
        :rtype: str
        """
        return self.session.get(self.base_url + f'/res.php?userkey={self.access_token}&id={captcha_id}').text
