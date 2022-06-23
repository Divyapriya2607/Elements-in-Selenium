import time

import chromedriver_autoinstaller
from selenium import webdriver

#driver = webdriver.chrome(executable_path="")
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        #time.sleep(5)
        if card_name == "Elements":
            #time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            card.find_element(By.XPATH, "//div/div[@class='avatar mx-auto white']").click()
            #time.sleep(3)
            print("clicked")
            menu_list = driver.find_elements(By.XPATH, "//div[@class='element-list collapse show']")
            for item in menu_list:
                Button_textbox=item.find_element(By.XPATH, "//div[@class='element-list collapse show']/ul/li").text
                #time.sleep(3)
                if Button_textbox == "Text Box":
                    #time.sleep(3)
                    item.find_element(By.XPATH, "//li[@id='item-0']").click()
                    print("textbox link clicked")
                    #time.sleep(2)
                else:
                    print("textbox not clicked")
            textbox_username = driver.find_element(By.XPATH, "//label[text()='Full Name']/following::input[@id='userName']")
            textbox_username.send_keys("Riya")
            print("username")
            textbox_email = driver.find_element(By.XPATH, "//label[text()='Email']/following::input[@id='userEmail']")
            textbox_email.send_keys("riya@gmail.com")
            print("email")
            #WebDriverWait(driver, 5).until(
                #EC.presence_of_element_located((By.XPATH, "//label[text()='Current Address']/following::textarea[@id='currentAddress']")))
            textarea_currentaddress = driver.find_element(By.XPATH, "//label[text()='Current Address']/following::textarea[@id='currentAddress']")
            textarea_currentaddress.send_keys("watson street")
            print("address")
            text_permanentaddress = driver.find_element(By.XPATH, "//label[text()='Permanent Address']/following::textarea[@id='permanentAddress']")
            text_permanentaddress.send_keys("Besant nagar")

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button_submit = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[@id='submit']")))
            button_submit.click()

            print("submit button clicked")
            time.sleep(5)

        else:
            print("Not clicked")
except:
    print("Elements not clicked")

