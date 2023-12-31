from selenium import webdriver
import schedule
from pynput.keyboard import Key, Controller
import time
from email.message import EmailMessage
import ssl
import smtplib

def update():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Still running: ")
    print(print(current_time))

def regKayCar(choice):

    def enter():
        keyboard.tap(Key.enter)
        lilSleep()

    def tab():
        keyboard.tap(Key.tab)
        lilSleep()

    def lilSleep():
        time.sleep(.3)

    if choice == 1:
        aptNum = "303D"
        phoneNum = "2741"

    elif choice == 2:
        aptNum = "303B"
        phoneNum = "2051"

    elif choice == 3:
        aptNum = "303A"
        phoneNum = "4558"

    keyboard = Controller()

    #go to website
    web = webdriver.Chrome()
    web.get('https://app.apartmentpermits.com/resident')

    time.sleep(2)

    #log in
    tab()

    for char in "The Retreat":
        keyboard.tap(char)

    time.sleep(3)

    enter()
    tab()
    tab()

    for char in aptNum:
        keyboard.tap(char)
    lilSleep()
    tab()

    for char in phoneNum:
        keyboard.tap(char)
    lilSleep()

    tab()
    enter()

    time.sleep(3)
    #after giving time to load in, navigate to add vehicle

    for x in range(5):
        tab()

    enter()
    tab()
    tab()
    enter()

    #enter in car information
    time.sleep(1)
    tab()
    tab()
    for char in "malibu":
        keyboard.tap(char)
    time.sleep(1)
    enter()

    tab()
    time.sleep(1)
    keyboard.tap(Key.down) #selects black
    keyboard.tap(Key.down)
    lilSleep()
    enter()

    tab()
    tab()
    for char in "SFV6524": #types in license plate
        keyboard.tap(char)
    lilSleep()

    tab()
    for char in "SFV6524":#confirms license plate
        keyboard.tap(char)
    lilSleep()

    tab()
    tab()

    enter()

    time.sleep(3)

    #sends an email confirming the car is registered, maybe later i can implement a screenshot?
    email_sender = 'fluffypants919@gmail.com'
    email_password = 'snvvefchgqpkjkgu'

    email_reciever = 'dylannorris919@gmail.com'

    subject = "Kaylie Car Registered"
    body = "Kaylie's car is registered!"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

#schedule.every().day.at("17:19").do(regKayCar)
#schedule.every().day.at("20:49").do(regKayCar)
#schedule.every(1).hours.do(update)
print("1 - Dylan")
print("2 - Nich")
print("3 - Versie")
choice = input("Whose name to register under: ")
choice = int(choice)

while choice != 1 and choice != 2 and choice != 3:
    choice = input("Try again: ")
    choice = int(choice)

regKayCar(choice)

#while True:
    #schedule.run_pending()
    #time.sleep(2)