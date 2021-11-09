import os
import webbrowser
import pyautogui as pt
import pyperclip
from time import sleep

print("Hello user, I am very glad to be your bot.\nI will try my best to assist your work.")
sleep(5)
try:
    browser=int(input("Please select Browser type\n1.Chrome\n2.Mozilla\n3.Default\n"))
    if(browser==1):
        webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open("https://accounts.google.com/AddSession/identifier?hl=en-GB&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    elif(browser==2):
        webbrowser.get("C:\Program Files\Mozilla Firefox\firefox.exe").open("https://accounts.google.com/AddSession/identifier?hl=en-GB&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    elif(browser==3):
        webbrowser.open("https://accounts.google.com/AddSession/identifier?hl=en-GB&continue=https%3A%2F%2Fmail.google.com&service=mail&ec=GAlAFw&flowName=GlifWebSignIn&flowEntry=AddSession")
    else:
        print("sorry we are unable to process your request")
        exit()
except:
    print("Sorry I am unable to proceed further, since you have not installed related libraries to run")
    exit()
while(True):
    position=pt.locateOnScreen("email.PNG",confidence=0.6)
    if(position!=None):
        break
    else:
        pass
x=position[0]
y=position[1]
def login():
    global x,y
    pt.moveTo(x+10,y+27)
    pt.click()
    pt.typewrite("email")
    pt.typewrite("\n")
    sleep(5)
    pt.typewrite("password")
    pt.typewrite("\n")
login()

            




