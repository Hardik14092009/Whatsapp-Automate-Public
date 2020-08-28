#This project automates Whatsapp
#imports webdriver from selenium
#Guidelines of the script:
#When this script runs please login on web.whatsappp.com  and open a chat in 60 seconds so that this script can locate desired elements
from selenium import webdriver
#importing time module
import time

#defining driver
#Using Chromedriver Here
driver = webdriver.Chrome(#Directory where chromedriver.exe is located)

#Opens web.whatsapp.com
driver.get("https://web.whatsappp.com/")

#using time.sleep for pausing the script for the given time so that user can login
time.sleep(60)
message = "Hello World"
messagebox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')#this is the current xpath of the chat box of whatsapp whick may change in future
#sending keys to messagebox
messagebox.send_keys(messagebox)
send_button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')#this is the current xpath of the send button of whatsapp whick may change in future
#clicking the send button
send_button.click()
