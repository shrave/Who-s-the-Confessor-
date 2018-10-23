import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

browser = webdriver.Chrome()

browser.get("https://m.facebook.com/iiithconfrevampd/")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

post_set = ()

while True:
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # for element in browser.find_elements_by_tag_name('div'):
        # post_set.add(browser.find_element_by_tag_name('div').text)
        print browser.find_element_by_tag_name('div').text
    except:
        continue

# for element in browser.find_elements_by_tag_name('div'):
# 	# if element.text:
# 	# 	print element.text
# 	# 	if element.text[0]=='#':
# 	# 		print "Success"
# 	print element.text
# print post_set

print ("done")
browser.quit()