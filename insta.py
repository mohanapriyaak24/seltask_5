from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.instagram.com/guviofficial/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.maximize_window()
sleep(3)
m = driver.find_element(By.XPATH, "//button[contains(.,'followers')]")
print("Total no. of followers ", m.text)

k = driver.find_element(By.XPATH, "//button[contains(.,'following')]")
print("Total no. of following", k.text)
