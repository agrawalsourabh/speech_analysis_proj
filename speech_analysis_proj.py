# import
import requests
import bs4
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL_SPEECH = "https://www.narendramodi.in/pms-address-to-the-nation-547268"
URL_LOGIN = "https://www.narendramodi.in"


def read_webpage(URL):
    print(URL_LOGIN)
    cred = {
        'LoginForm[user_email]': 'agrawal.sourabh644@gmail.com',
        'LoginForm[password]': 'Sourabh@12345@',
        'page_url': "index"
    }
    page = requests.get(url=URL_LOGIN, params=cred)
    print(page.url)
    print("Status code: " + str(page.status_code))
    soup = bs4.BeautifulSoup(page.content, "html.parser")

    print(soup.title)



read_webpage("https://www.narendramodi.in/pms-address-to-the-nation-547268")

