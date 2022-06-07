import time

import chromedriver_autoinstaller
from selenium import webdriver

#driver = webdriver.chrome(executable_path="")
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chromedriver_autoinstaller.install()

driver = webdriver.Chrome(service=Service(), options=chrome_options)
driver.get("https://demoqa.com/")
try:
    cards = driver.find_elements(By.XPATH, "//div[@class='card mt-4 top-card']")

    for card in cards:
        card_name = card.find_element(By.XPATH, "div/div/h5").text
        print(card_name)
        time.sleep(5)
        if card_name == "Elements":
            print("Clicked")
            time.sleep(5)
            card.find_element(By.XPATH, "//div[@class='card-body']").click()
            print("Clicked")
            time.sleep(3)
        else:
            print("failed")

except:
    print("Finished")





