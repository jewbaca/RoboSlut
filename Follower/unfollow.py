from selenium import webdriver
import time
import autoit
import os
import requests
import csv
import requests
from random import *


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
time.sleep(3)


url = "https://instagram.com/futurefactz/"
# time.sleep(.2)
autoit.send("{F6}")
# time.sleep(.2)
autoit.send(url)
autoit.send("{ENTER}")
time.sleep(1)
autoit.send("{F5}")


try:

	autoit.send("{TAB 6}")
	time.sleep(1)
	autoit.send("{ENTER}")
	time.sleep(3)
	autoit.send("{F5}")
	time.sleep(3)
	autoit.send("{TAB 6}")
	time.sleep(1)
	autoit.send("{ENTER}")
	time.sleep(3)

	i=0
	while (i < 240):
		i = i +3
		time.sleep(.5)
		blah = '"{TAB %s}"' % i
		print blah
		time.sleep(.5)
		autoit.send(blah)
		autoit.send("{SPACE}")
		time.sleep(26)

except:
	print "fuck this shit"




 #   if tetha == "Like":

    #      print "clickjustexecuted on %s" % line

    #flawless
