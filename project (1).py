from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser as wb
import smtplib
import requests
import sys
from selenium import webdriver
from weather import Weather
import time
"""from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException"""

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
    #use the system's inbuilt say command instead of mpg123
    #text_to_speech = gTTS(text = audio, lang = 'en', slow = False, lang_check = True)
    #text_to_speech.save('audio.mp3')
    #os.system('mpg321 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()  #Initialize the recognizer
    with sr.Microphone() as source:  #use the microphone as source for input
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  #energy threshold(A threshold is an amount, level, or limit on a scale) based on the surrounding noise level
        audio = r.listen(source)  #listens for the user's input

    try:
        command = r.recognize_google(audio).lower()   #error occurs when google could not understand what was said
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"

    #yukta
    
    if 'up' in command:
        talkToMe('Machi Readiya?')

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

   
    elif 'contact' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()
        sendto=""

        if 'office' in recipient:
            sendto='yuktajain11@gmail.com' #'info@bmsce.ac.in'
            p='80-26622130-35'
                 
        elif 'placement' in recipient:
            sendto='bmsceplacement@gmail.com'
            p='80-26622130-31'

        elif 'library' in recipient:
            sendto='drnch.lic@bmsce.ac.in'
            p='80-26622130-32'

        elif 'data center' in recipient:
            sendto= 'cheifcoordinator@bmsce.ac.in'
            p='80-26622130-33'
            
        elif 'data center' in recipient:
            sendto='cheifcoordinator@bmsce.ac.in'
            p='80-26622130-37'
        

        else:
            talkToMe('I don\'t know what you mean!')
            return

        
        talkToMe('Call or email?')
        c=myCommand()

        if 'email' in c:
            talkToMe('What should I say?')
            content = myCommand()
            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            #identify to server
            mail.ehlo()
            #encrypt session
            mail.starttls()
            #login
            mail.login('srishtirathi963@gmail.com', '1!2@3#srishti')       
            #send message
            mail.sendmail('srishtirathi963@gmail.com',sendto, content)
            talkToMe('Email sent.')        
            #end mail connection
            mail.close()

        elif ('phone' in c) or ('call' in c):
            print('Contact no: ',p)

        else:
            talkToMe('I don\'t know what you mean!')



            
   #srishti

    if 'hostel' in command:
        wb.get().open_new("http://www.bmsce.in/home/About-BMSET-Hostels")
        print('Done!')
       
    elif 'hospital' in command:
        wb.get().open_new("http://www.bmsce.in/home/BMS-Hospital")
        print('Done!')
       
    elif 'library' in command:
        wb.get().open_new("http://www.bmsce.in/home/About-Library")
        print('Done!')  
       
    elif 'data centre' in command:
        wb.get().open_new("http://www.bmsce.in/home/About-Data-Center")
        print('Done!')  
    elif 'sports' in command:
        wb.get().open_new("http://www.bmsce.in/home/About-Sports")
        print('Done!')    
       
       
    elif 'counselling centre' in command:
        wb.get().open_new("http://www.bmsce.in/home/Counselling-Center")
        print('Done!')
    elif 'exit' in command:
        print("turning off...")
        sys.exit()

    #vaishnavi

    if ('department' in command)  or ('syllabus' in command)  or ('faculty' in command) or ('research' in command) or ('publication' in command):
        talkToMe('Which dep?')
        dept = myCommand().lower()
        url_txt=""

        if 'cs' in dept or 'computer science' in dept:
            url_txt = 'Computer-Science-and-Engineering'

        elif 'civil' in dept.lower():
            url_txt = 'Civil-Engineering'

        elif 'mech' in dept.lower():
            url_txt = 'Mechanical-Engineering'

        elif 'eee'in dept or 'electrical' in dept or 'electronics' in dept.lower():
            url_txt = 'Electrical-and-Electronics-Engineering'
                 
        elif 'iem' in dept or 'industrial engineering' in dept or 'industrial engineering and management' in dept.lower():
            url_txt = 'Industrial-Engineering-and-Management'

        elif 'ec' in dept or 'tc' in dept or 'electronics' in dept or'telecommunication' in dept.lower():
            url_txt = 'Electronics-and-Telecommunication-Engineering'

        elif 'is' in dept or 'information science' in dept.lower():
            url_txt = 'Information-Science-and-Engineering'

        elif 'eie' in dept or 'instrumentation' or 'electronics and instrumentation' in dept.lower():
            url_txt = 'Electronics-and-Instrumentation-Engineering'

        elif 'ml' in dept or 'medical electronics' in dept.lower():
            url_txt = 'Medical-Electronics'

        elif 'chemical' in dept or 'chem' in dept.lower():
            url_txt = 'Chemical-Engineering'

        elif 'bt' in dept or 'bio tech' in dept or 'bio-tech' in dept.lower():
            url_txt = 'Bio-Technology'

        elif 'mca' in dept or 'computer applications' in dept.lower():
            url_txt = 'Computer-Applications-MCA'

        elif 'mba' in dept or 'business administration' in dept.lower():
            url_txt = 'Master-of-Business-Administration'

        elif 'math' in dept.lower():
            url_txt = 'Mathematics-Department'

        elif 'physics' in dept.lower():
            url_txt = 'Physics-Department'

        elif 'chemistry' in dept.lower():
            url_txt = 'Chemistry-Department'

        elif 'aerospace' in dept.lower():
            url_txt = 'Aerospace-Engineering'
                 
        else:
            talkToMe('There\'s no such department in BMSCE!')
            return

        if 'department' in command:
            url = 'http://www.bmsce.in/home/' + url_txt + '-About'

        elif 'syllabus' in command:
            url = 'http://www.bmsce.in/home/' + url_txt + '-Syllabus'

        elif 'faculty' in command:
            url = 'http://www.bmsce.in/home/' + url_txt + '-Faculty'

        elif 'publication' in command:
            url = 'http://www.bmsce.in/home/' + url_txt + '-Publications'

        elif 'research' in command:
            url = 'http://www.bmsce.in/home/' + url_txt + '-Research'

   

        driver=webdriver.Chrome("C:\\Users\YUKTA JAIN\Documents\chromedriver.exe")
        driver.get(url)
#shubh
    elif 'admission' in command:
        talkToMe('which type of admission?')
        search = myCommand()
        if 'under grad' in search or 'ug' in search:
                wb.get().open_new("http://bmsce.ac.in/home/Under-Graduation")
        elif 'post grad' in search or 'pg' in search:
                wb.get().open_new("http://bmsce.ac.in/home/Post-Graduation")
        elif 'phd' in search:
                wb.get().open_new("http://www.bmsce.in/home/PhD")
        elif 'international'  in search or 'nri' in search:
                wb.get().open_new("http://bmsce.ac.in/home/International-Admissions")

    elif ('calendar' in command) or ('events' in command):
        wb.get().open_new("http://bmsce.ac.in/home/Calendar-of-Events")
                       
    elif ('notification' in command) or ('result' in command):
        wb.get().open_new("http://bmsce.ac.in/home/COE-Notifications")
                      
    elif ('recruit' in command) or ('companies' in command):
        wb.get().open_new("http://bmsce.ac.in/home/Placement-Recruiting-Companies")

        
    elif ('placement' in command) or ('stats' in command):
        wb.get().open_new("http://bmsce.ac.in/home/Placement-Statistics")

        
    elif 'videos' in command:
        wb.get().open_new("http://bmsce.ac.in/home/Education-Videos")

    elif ('month' in command) or ('activit' in command):
        wb.get().open_new("http://bmsce.ac.in/home/BMSCE-Monthly-Activities")

    elif 'scholarship' in command:
        wb.get().open_new("http://bmsce.ac.in/home/Scholarships")

       

    
talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
