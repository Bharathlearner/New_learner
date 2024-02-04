"""import pywinauto
from pywinauto import Application

app = Application(backend="uia").start('Notepad.exe')
dlg = app.window().maximize()
dlg1 = app.window(title='Untitled - Notepad')
dlg1.print_control_identifiers()
dlg1."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
import os
from shutil import copy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec