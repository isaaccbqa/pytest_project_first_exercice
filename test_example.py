import pytest
import time
from pages.home_page import home_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 


@pytest.fixture
def browser():
    # Ruta al archivo chromedriver.exe
    chrome_driver_path = "chromedriver-win64\\chromedriver.exe"
    appPath = "C:\\Users\\JoséIsaacFloresCasti\\AppData\\Local\\Programs\\qx_insight\\QX Insight.exe"  # noqa
    # Crear opciones para el navegador Chrome
    chrome_options = Options()
    chrome_options.binary_location = appPath
    # Inicializa el servicio del ChromeDriver
    service = Service(executable_path=chrome_driver_path)
    # service.start()
    # Inicializa el WebDriver de Chrome
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    # Cierra el navegador después de la prueba
    driver.quit()


def test_create_new_plate(browser):
    # assert "Google" in browser.title
    time.sleep(5)
    homePage = home_page(browser)
    homePage.testCreateNewPlate()
