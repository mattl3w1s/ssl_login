import requests
import lxml
from ssl_login.locators import Locators
from ssl_login.actions import Actions

class Site(object):

    def __init__(self,login_dict={'username':'','password':''}):
        self.Locators = Locators
        self.Actions = Actions
        self.payload = {
            Locators.username:login_dict["username"],
            Locators.password:login_dict["password"]
        }

    def login(self):
        pass