
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
import pandas as pd
import re
import numpy as np
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
time.sleep(3)


code_phone = int(input("Input the code sent to your phone: "))
input_field_code = driver.find_element_by_xpath("//div[@class='input-field']//input[1]")
input_field_code.send_keys(code_phone)

time.sleep(6)
#michael franco data peer id
#1015336350

#clicks on test chat with messages
peer_chat = driver.find_element_by_xpath("//li[@data-peer-id='-1572277888']")
peer_chat.click()

time.sleep(6)


#check if message a member of set
#if message is not a member of the set
#then add message to dictionary



driver.set_window_size(590, 1000)


top_message_element = driver.find_element_by_class_name('message')

while True:
    messages = driver.find_elements_by_class_name('message')
    time.sleep(2)

    for i, message in enumerate(messages):
        if message.text not in membership_check_set and len(message.text) > 20:

            print("This is message: ")
            print(message_count)
            #gets the length of the header, category line
            first_line = message.text.partition('\n')[0]
            #Place logic to handles different separaters
            #separators such as | or space or ,
            #If len(message.split()) > len(message.spllit(,):
            #  first_line_list = first_line.split()


            first_line_list = first_line.split(',')
            len_first_line = len(first_line_list)

            #List SLicing could help here
            #https://www.geeksforgeeks.org/python-list-slicing/


            # turn message into a list
            my_string = message.text



            #at this point, it produces a list of each line within the quotes
            string_list = re.split(', |\n|!', message.text)



            print("Here is the String List")
            print(string_list)

            lines_num = len(string_list)
            print("Here is len of String list:")
            print(lines_num)

            string_list_indiv=[]
            for i, line in enumerate(string_list):
                string_list_indiv += line.split(',')

            print(string_list_indiv)



            print("TEST LIST SLICE BELOW: ")
            #removes the elements of the views and the time from the list
            string_list_indiv.pop()
            string_list_indiv.pop()

            row_records_list = []
            #need to get the number of rows here in order to create np array and reshape
            for i in range(0, len(string_list_indiv), len_first_line):
                row_records_list += [string_list_indiv[i:i + len_first_line]]

            print("Row Records List")
            print(row_records_list)
            len_rows = len(row_records_list)

            #the string without the columns headers
            #print(string_list_indiv[len_first_line:])

            df = pd.DataFrame(np.array(string_list_indiv[len_first_line:]).reshape(len_rows-1, len_first_line), columns=first_line_list)






            print(first_line_list)
            print("First line length")
            print(len(first_line_list))

            # determining the name of the file
            file_name = 'message_'+str(message_count)+'_WillsData.xlsx'

            # saving the excel
            df.to_excel(file_name)









            membership_check_set.add(message.text)

            message_count += 1




    time.sleep(2)
    top_message_element = ".bubble-content-wrapper > .bubble-content > .message"
    scroll = "document.querySelector(\'" + top_message_element + "\').scrollIntoView();"
    driver.execute_script(scroll)  # execute the js scroll
    time.sleep(2)  # wait for page to load new content

    if message_count > 3:
        break

outFile = open('dictionary.py', 'w')
outFile.write(str(final_dictionary))

print("FINAL DICTIONARY")
print("Message Count: ")
print(message_count)
print(str(final_dictionary))

#Log

#9/27/2021

#the problem is that the String List len is not accurate. it's breaking each row
#need to figure out how to fix


#Helpful links
#https://stackoverflow.com/questions/39428042/use-selenium-with-chromedriver-on-mac
#https://medium.com/analytics-vidhya/using-python-and-selenium-to-scrape-infinite-scroll-web-pages-825d12c24ec7
#https://www.kite.com/python/answers/how-to-fill-a-pandas-dataframe-row-by-row-in-python
#https://stackoverflow.com/questions/42593104/convert-list-into-a-pandas-data-frame