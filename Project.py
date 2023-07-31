v=2
# v take as the time to sleep between clicks depending on internet speed
from temp import *
from links import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.pesuacademy.com/Academy/")
#element = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.ID, "j_scriptusername")))
elem = driver.find_element_by_name("j_username")
elem.clear()
#global user_name
#user_namef = Guilogin.sendval(user_name) #retriving info from other files
elem.send_keys(user_name)
#elem.send_keys('PES2UG20CS')
elem = driver.find_element_by_name("j_password")
elem.clear()
#global user_pass
#user_passf = Guilogin.sendval(user_pass) #retriving info from other files
elem.send_keys(user_pass, Keys.RETURN)
#elem.send_keys('pass***', Keys.RETURN)
#elem.send_keys(Keys.RETURN)
assert 'Your Username and Password do not match' not in driver.page_source
element = WebDriverWait(driver, 500).until(EC.element_to_be_clickable((By.ID, 'menuTab_653')))
time.sleep(v)
My_courses = driver.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]/a/span[2]').click()
time.sleep(v)
#s_a1 = Gui.sendval(s_a)
S_ubject = driver.find_element_by_xpath(link[s_a]).click()
time.sleep(v)
#s_a1 = Gui.sendval(s_u)
U_nit = driver.find_element_by_xpath(link[s_u]).click()
time.sleep(v)
#final_link1 = Gui.sendval(final_link)
R_source = driver.find_element_by_xpath(final_link).click()
time.sleep(v)
import os
if os.path.exists('temp.py'):
    os.remove('temp.py')
        
else:
    dis_pop = Tk(className = 'Aboubt')
    dis_pop.iconbitmap('C:/Users/suraj/Desktop/New folder/Final/icon.ico')
    dis_pop.geometry("300x400")
    
    Dis_play=Label(dis_pop, text='Your credentials are not safe kindly delete the files phyisically', bg='grey', fg='Red',width=30, height=15,font=("Arial", 20)).pack()
    E_it = Button(dis_pop, text='OK' , command=dis_pop.destroy, font=('Arial', 10),fg='Red').pack()
    dis_pop.mainloop()
'''
#My_courses = WebDriver.findElement(By.Id('menuTab_653')).Click()
subject = driver.find_element_by_id(#input for Subject).click()
unit = driver.find_element_by_id(#input for Unit).click()
chapter = driver.find_element_by_id(#input for chapter).click()
'''


#using time.sleep(x) worked
#use wait compulsory
# continue with 3rd