from selenium import webdriver
import autoit
import os
import time

driver = webdriver.Chrome()
driver.get("https://instagram.com/")
login_elem = driver.find_element_by_xpath("//article/div/div/p/a[text()='Log in']")
login_elem.click()

autoit.send("futurefactz")
autoit.send("{TAB}")
autoit.send("caremamanuel")
autoit.send("{TAB}")
autoit.send("{TAB}")
autoit.send("{ENTER}")


with open('data.txt') as f:
    for line in f:
        url = "https://instagram.com/%s" % line
        print url
        autoit.send("{F6}")
        time.sleep(3)
        autoit.send(url)
        autoit.send("{ENTER}")
        time.sleep(3)
        autoit.send("{F5}")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div[1]/div[1]").click()
        #autoit.send("{TAB}")
        #autoit.send("{TAB}")
        #autoit.send("{TAB}")
        #autoit.send("{TAB}")
        #autoit.send("{TAB}")
        #autoit.send("{TAB}")
        #autoit.send("{ENTER}")
        #time.sleep(1)
        
        pause
        

