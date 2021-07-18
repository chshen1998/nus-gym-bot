from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getSlots(driver_path):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get("https://reboks.nus.edu.sg/nus_public_web/public/profile/buypass/gym")

    return driver.title

