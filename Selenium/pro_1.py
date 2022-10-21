from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("C:/Users/alokkDownloads/Compressed/chromedriver_win32/chromedriver.exe")
driver.get('https://www.google.co.in/maps/@27.141237,80.8833819,7z')
def searchPlace():
    place = driver.find_element_by_class_name('tactile-searchbox-input')
    place.send_keys('varanasi')
    Submit = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button')
    Submit.click()
searchPlace()

def direction():
    sleep(10)
    direction = driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div/button/img')
    direction.click()
direction()