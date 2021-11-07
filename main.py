import os
import webbrowser
import pyautogui as pt
import pyperclip
from time import sleep

webbrowser.open("https://accounts.google.com/AddSession/identifier?hl=en-GB&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
sleep(5)
position=pt.locateOnScreen("email.PNG",confidence=0.6)
x=position[0]
y=position[1]
pt.moveTo(x+10,y+27)
pt.click()
pt.typewrite("pavananudeepmotiki@gmail.com")
pt.typewrite("\n")
sleep(5)
pt.typewrite("Manjula@9")
pt.typewrite("\n")
