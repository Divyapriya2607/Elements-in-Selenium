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

cards = driver.find_elements(By.XPATH, "//div[@class='card mt-4 top-card']")
try:
    for card in cards:
        card_name = card.find_element(By.XPATH, "//div/div[@class='card-body']/h5").text
        print(card_name)
        time.sleep(5)
        if card_name == "Elements":
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            card.find_element(By.XPATH, "//div/div[@class='avatar mx-auto white']").click()
            time.sleep(3)
            print("clicked")
            menu_list = driver.find_elements(By.XPATH, "//div[@class='element-list collapse show']")
            for item in menu_list:
                Button_textbox=item.find_element(By.XPATH, "//div[@class='element-list collapse show']/ul/li").text
                time.sleep(3)
                if Button_textbox == "Text Box":
                    time.sleep(3)
                    item.find_element(By.XPATH, "")


        else:
            print("Not clicked")
except:
    print("Elements not clicked")

