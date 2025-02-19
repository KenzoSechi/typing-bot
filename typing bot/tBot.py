import pyautogui
import time

text = open('text')

time.sleep(3) # To open the textfield to fill


for line in text:
    pyautogui.typewrite(line)
    time.sleep(0.01)
