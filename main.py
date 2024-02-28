from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument("disable-link-features=AutomationControlled")
chrome_options.add_argument("start-maximized")

#try other opetions

PRODUCT_NAME = input("Enter product you want to buy: ")
priceRange = input("Enter price range in this format:  xxx-xxx\n")
lowestPrice = priceRange.split("-")[0]
highestPrice = priceRange.split("-")[1]

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.elgiganten.se/")

time.sleep(1)
cookieAccept = driver.find_element(By.XPATH,value='//*[@id="coiPage-1"]/div[2]/button[2]')
cookieAccept.click()

searchButton = driver.find_element(By.NAME,value="search")
searchButton.click()

searchButton.send_keys(PRODUCT_NAME)
searchButton.send_keys(Keys.ENTER)

time.sleep(1)

lowestNumber = driver.find_element(By.XPATH,value='//*[@id="main"]/ng-component/elk-product-listing/div[2]/aside/elk-component-loader-wrapper/elk-filter/elk-filter-groups/ff-asn/ff-asn-group-slider/div[2]/div/ff-slider-control/div/div/input[1]')
lowestNumber.click()
time.sleep(1)
lowestNumber.send_keys(Keys.CONTROL,'a')
lowestNumber.send_keys(Keys.BACK_SPACE)

lowestNumber.send_keys(lowestPrice)

highestNumber = driver.find_element(By.XPATH,value='//*[@id="main"]/ng-component/elk-product-listing/div[2]/aside/elk-component-loader-wrapper/elk-filter/elk-filter-groups/ff-asn/ff-asn-group-slider/div[2]/div/ff-slider-control/div/div/input[2]')
highestNumber.click()
time.sleep(1)
highestNumber.send_keys(Keys.CONTROL,'a')
highestNumber.send_keys(Keys.BACK_SPACE)

highestNumber.send_keys(highestPrice)

highestNumber.send_keys(Keys.ENTER)

print("DONE")

