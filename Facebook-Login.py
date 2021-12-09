from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = ("D:\Education\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(PATH)

driver.get("https://www.facebook.com/")

search1 = driver.find_element_by_name("email")
search1.send_keys("your email")
search2 = driver.find_element_by_name("pass")
search2.send_keys("your password")
search1.send_keys(Keys.RETURN)
