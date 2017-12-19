from selenium import webdriver
import time
import autoit
import os
import requests
import json
import urllib
import wget
import urllib2
import csv
import requests
from pprint import pprint
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://instagram.com/")
login_elem = driver.find_element_by_xpath("//article/div/div/p/a[text()='Log in']")
login_elem.click()

autoit.send("brozada_")
autoit.send("{TAB}")
autoit.send("caremamanuel")
autoit.send("{TAB}")
autoit.send("{TAB}")
autoit.send("{ENTER}")
count = 0

with open('data3.txt') as f:
    for line in f:
        url = "https://instagram.com/" + line.strip()
        urlj = "" +  line.strip()
      #  urlj = "https://instagram.com/%s/?_a=1" % line
        #urlb = url.strip('\n')
       # urlc = "'{}'".format(url)
        #print urlc
        r = requests.get(url)
        #print r.text.encode('utf-8')
        data = r.text.encode('utf-8')
    
        #urlc = pprint(urlb)
        #this only works when hard corded for some reason
    #    web_page = urllib2.urlopen(urlc)
        linel = line[:-2]
        
        with open(linel + ".csv", 'w') as f:
            f.write(data)
            
        time.sleep(3)
        
        with open(linel + ".csv", 'r') as f:
            r = list( csv.reader(f) )
            try:
              something = r[158][51]
              string = something[10:-1]
            except: 
              string = "dodo"
              print "link is probably unavailable"

        time.sleep(.5)
        #with open(filen, 'r') as f:
         #   r = list( csv.reader(f) )
         #   something = r[158][51]
        #time.sleep(.5)
        '''autoit.send("{F6}")
        time.sleep(.5)
        autoit.send(url)
        autoit.send("{ENTER}")
        time.sleep(.5)'''
        
        #print string
       # alpha = driver.find_element_by_xpath('//html/body/span/section/main/article/div[3]/div[1]/div[1]/div[1]')
        #print alpha
       # time.sleep(.5)
        #alpha.lick()


        newurl = "https://instagram.com/p/%s/?taken-by=%s" % (string, line)
       # time.sleep(.2)
        autoit.send("{F6}")
       # time.sleep(.2)
        autoit.send(newurl)
        time.sleep(.2)
        autoit.send("{ENTER}")
        time.sleep(.2)

        try:
          beta = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/a[1]/span[contains(text(), "Like")]')
          beta.click()
          time.sleep(3)
          autoit.send("{F5}")
          count = count + 1
          print urlj
          print count
          
        except:
          
          continue

        

     #   if tetha == "Like":
              
        #      print "clickjustexecuted on %s" % line

        #flawless
        
        
        

