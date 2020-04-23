from selenium import webdriver
from pynput.mouse import Controller
import pyautogui
import time

mouse = Controller()

print(mouse.position)

driver = webdriver.Chrome("C:/Users/samta/OneDrive/Programacao/Python/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Who do you want to ban? : ')

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
loca = str(user.location)
print(loca)

if(loca[20] != "}"):
    locaX = loca[6] + loca[7] + loca[8] + loca[9]
    locaY = loca[17] + loca[18] + loca[19] + loca[20]
    locaY = int(locaY)

else:
    locaX = loca[6] + loca[7] + loca[8] + loca[9]
    locaY = loca[17] + loca[18] + loca[19]
    locaY = int(locaY)

mouse.position = (locaX, locaY + 40)

pyautogui.click(button='right')

pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('enter')
mouse.position = (785, 426)
pyautogui.click()

time.sleep(2)
