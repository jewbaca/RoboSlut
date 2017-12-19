from selenium import webdriver
import time
import autoit
import os
import requests
import csv
import requests
from pprint import pprint
from random import *
from itertools import repeat
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os.path

#binary = FirefoxBinary('O:\\Program Files\\Mozilla Firefox\\firefox.exe')
##path = "O:\\Jew\Desktop\\Robo\\Follower\\geckodriver.exe"
driver = webdriver.Chrome()
driver.get("https://instagram.com/")


login_elem = driver.find_element_by_xpath("//article/div/div/p/a[text()='Log in']")
login_elem.click()

autoit.send("")
autoit.send("{TAB}")
autoit.send("")
autoit.send("{TAB}")
autoit.send("{TAB}")
autoit.send("{ENTER}")
count = 0
meh = randint(60,600)
multi = autoit.send("{TAB}")

with open('names.txt') as f:
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
        ehe = linel + ".csv"

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
        autoit.send("{ENTER}")
        time.sleep(3)
        autoit.send("{F5}")
        time.sleep(3)


        
        try:
          beta = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/a')
          print "this ran once"
          beta.click()
          time.sleep(1)
         # autoit.send("{TAB 5}")
        #  time.sleep(.5)
        #  autoit.send("{SPACE}")
         # time.sleep(.5)
          i = 3
          while (i < 150):
              #time.sleep(5)
              blah = '"{TAB %s}"' % i
              print blah
              #time.sleep(.5)
              autoit.send(blah)
              time.sleep(.3)
              autoit.send("{SPACE}")
              time.sleep(30)
              autoit.send("{HOME}")
              autoit.send("{TAB}")
              time.sleep(.5)
              i = i + 3
       #   for x in range(0,len(heta)):
        #        if heta.text == 'Follow':
        #            heta[x].send_keys("\n")

          for line_number, line in enumerate(fileinput.input('names.txt', inplace=1)):
            if line_number == 0:
              continue
            else:
              sys.stdout.write(line)
        except:
          print "fuck this shit"
     
          continue
     
     #   if tetha == "Like":

        #      print "clickjustexecuted on %s" % line

        #flawless
