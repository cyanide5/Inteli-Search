from selenium import webdriver
from selenium.webdriver.common.keys import Keys



i = str(input("Enter Search Terms: "))

browser = webdriver.Chrome()

browser.get("https://cse.google.com/cse?cx=005277190761971209795:aj_c6-y2zes")

searchBar = browser.find_element_by_id('gsc-i-id1')

searchBar.send_keys(i)
searchBar.send_keys(Keys.ENTER)





