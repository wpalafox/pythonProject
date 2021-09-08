
#from urllib.request import urlopen
#from bs4 import BeautifulSoup

#import requests
#from lxml import html
#https://medium.com/@kikigulab/how-to-automate-opening-and-login-to-websites-with-python-6aeaf1f6ae98



#Pseudocode
#go to "web.telegram.org/k/
#click <button class="btn-primary btn-secondary btn-primary-transparent primary rp">
#input number to <div contenteditable="true" class="input-field-input"
#wait until user inputs code into code variable (asyncrio)?
#enter number in to name 127609635493299

#session_requests = requests.session()
#result = session_requests.get(login_url)

from selenium import webdriver
import credentials
import selenium
import os
import time
from selenium.webdriver.common.keys import Keys
import json
from datetime import date, datetime
import asyncio
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
url = "https://web.telegram.org/k/"


#Code to set up Chrome Driver
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
driver = webdriver.Chrome(executable_path = DRIVER_BIN)
browser = driver.get(url)
phone= credentials.phone_number
time.sleep(5)
membership_check_set = set()
final_dictionary = {}
message_count=0
scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec






# getting the button by class name
button = driver.find_element_by_class_name("btn-primary")

# clicking on the button
button.click()

time.sleep(2)

#look into targeting the input field by x-path instead of class

input_field_phone = driver.find_element_by_xpath("//div[@inputmode='decimal']")

input_field_phone.send_keys(phone)

# getting the button by class name
button = driver.find_element_by_class_name("btn-primary")

# clicking on the button
button.click()
time.sleep(2)


code_phone = int(input("Input the code sent to your phone: "))
input_field_code = driver.find_element_by_xpath("//div[@class='input-field']//input[1]")
input_field_code.send_keys(code_phone)

time.sleep(4)
#michael franco data peer id
#1015336350

#clicks on test chat with messages
peer_chat = driver.find_element_by_xpath("//li[@data-peer-id='-1572277888']")
peer_chat.click()

time.sleep(4)


#check if message a member of set
#if message is not a member of the set
#then add message to dictionary



driver.set_window_size(590, 1000)


top_message_element = driver.find_element_by_class_name('message')

while True:
    messages = driver.find_elements_by_class_name('message')
    time.sleep(2)

    for i, message in enumerate(messages):
        if message.text not in membership_check_set:
            membership_check_set.add(message.text)
            final_dictionary[message_count] = {message.text}
            message_count += 1

    time.sleep(2)
    top_message_element = ".bubble-content-wrapper > .bubble-content > .message"
    scroll = "document.querySelector(\'" + top_message_element + "\').scrollIntoView();"
    driver.execute_script(scroll)  # execute the js scroll
    time.sleep(2)  # wait for page to load new content

    if message_count > 2:
        break

outFile = open('dictionary.py', 'w')
outFile.write(str(final_dictionary))

print("FINAL DICTIONARY")
print("Message Count: ")
print(message_count)
print(str(final_dictionary))






#Helpful links
#https://stackoverflow.com/questions/39428042/use-selenium-with-chromedriver-on-mac
#https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7