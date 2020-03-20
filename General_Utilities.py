### Import Libs
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.2)
