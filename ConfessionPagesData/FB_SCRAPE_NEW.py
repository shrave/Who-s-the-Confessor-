import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup



chrome_options = Options()
# chrome_options.add_argument("--headless")
browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',chrome_options=chrome_options)

handle = "iiithconfrevampd"
browser.get("https://m.facebook.com/"+str(handle))
time.sleep(1)

elem = browser.find_element_by_tag_name("body")


post_set = ()

# while True:
#	 try:
#		 browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#		 # for element in browser.find_elements_by_tag_name('div'):
#		 # post_set.add(browser.find_element_by_tag_name('div').text)
#		 print browser.find_element_by_tag_name('div').text
#	 except:
#		 continue

scrollCount = 0
lastHeight = browser.execute_script("return document.body.scrollHeight")
while True:
	scrollCount += 1
	print("Scroll "+str(scrollCount))
	browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	time.sleep(1)
	newHeight = browser.execute_script("return document.body.scrollHeight")
	if newHeight == lastHeight:
		break
	lastHeight = newHeight

print ("done")
browser.quit()