import requests
import lxml
from ssl_login.locators import Locators
from ssl_login.actions import Actions

class Site(object):

    def __init__(self,LOGIN_ACTION):
        self.LOGIN_ACTION = LOGIN_ACTION
        self.Locators = Locators

    def login(self):
        pass