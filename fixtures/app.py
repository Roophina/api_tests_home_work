from fixtures.auth.api import Auth
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.user_info.api import UserInfo


class StoreApp:
    def __init__(self, url):
        self.url = url
        self.client = Client
        self.register = Register(self)
        self.auth = Auth(self)
        self.user_info = UserInfo(self)
