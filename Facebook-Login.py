from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Email = input("write you email or phone number")
Password = input("enter your password")

PATH = ("{the path of the msedgedriver}\msedgedriver.exe") 
driver = webdriver.Edge(PATH)

driver.get("https://www.facebook.com/")

search1 = driver.find_element_by_name("email")
search1.send_keys(Email)
search2 = driver.find_element_by_name("pass")
search2.send_keys(Password)
search1.send_keys(Keys.RETURN)
