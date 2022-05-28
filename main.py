import speech_recognition as sr     #convert speech to text
import datetime                     #for fetching date and time
import  time                        #time
import wikipedia
import cv2                          #camera
from bs4 import BeautifulSoup       #extract data out of HTML and XML files
import webbrowser                   #allow displaying web-based documents to user
import requests                     #allows you to send HTTP requests
import smtplib                      #mail
import playsound
import subprocess
import random
from selenium import webdriver
#lock window
#to play saved mp3 file
#import pyglet
import pyjokes                      #jokes
from gtts import gTTS               #google text to speech
import os                           #to save/open files
from plyer import notification      #access the features of the hardware
import wolframalpha                 #to calculate strings into formula

#print("hello world")
#send mail

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}



## smart assistant

def fun():
    respond("Switched to smart version. File is loading...")
    import emotion
    answer=[]
    respond("Activated..")
    respond("Hey I am your assistant chitti two point O with additional functionality of sentiment analysis")
    respond("Reply my questions i will help you according to your sentiment")
    respond("What is your name")
    text = talk().lower()
    respond("What is your profession")
    text = talk().lower()
    respond("how are you")
    text = talk().lower()
    answer.append(text)
    respond("how is your day going")
    text = talk().lower()
    answer.append(text)
    respond("Did you find your day productive")
    text = talk().lower()
    if 'yes' in text:
        text="yes Its very productive day"
    else:
        text = "no Its not productive day"
    answer.append(text)

    ##2-3 more questions
    res=emotion.predict(answer)
    respond("Chitti got your emotion")
    #respond(res)
    if(res=='happy'):
        respond("You are happy listen this song and make your day more beautiful")
        webbrowser.open("https://www.youtube.com/watch?v=_ae2j9jZY_U&t=128s")
        time.sleep(20)
        ##songs
    elif(res=='sad'):
        respond("Once Lemony Snicket said The way sadness works is one of the strange riddles of the world. If you are stricken with a great sadness, you may feel as if you have been set aflame, not only because of the enormous pain but also because your sadness may spread over your life, like smoke from an enormous fire. So always be motivated and be happy")
        respond("Listen this video perhaps it will help you in making you more confident")
        webbrowser.open("https://www.youtube.com/watch?v=tNN8JCf4Wms")
        time.sleep(20)
        ##motivational quotes and videos
    else:
        respond("oooh its good to see you are in neutral mood")
        respond("listen this song it will help you in making mood more happy sadabahaar songs")
        webbrowser.open("https://www.youtube.com/watch?v=ndE-4vLc1IE")
        time.sleep(20)
        ##sadabahar songs

#wish according to time

def wishMe():
    hour = int(datetime.datetime.now().hour) ##store time in hour

    if hour >= 4 and hour < 12:
        respond("Hello Good Morning!")

    elif hour >= 12 and hour < 18:
        respond("Hello Good Afternoon !")

    else:
        respond("Hello Good Evening")

    assname = ("Chitti 1 point o")   ##giving name to my assistant
    respond(f"I am your assistant {assname}")

##respond function ->text will convert to voice here ...what will my assistant said is here
def respond(output):
    print("Responding...")
    num = 0
    print(output)
    num += 1
    response = gTTS(text=output, lang='en',tld="com")
    file = str(num)+'.mp3'
    file = str(file)
    #print(file)
    response.save(file)
    playsound.playsound(file)
    #playsound.playsound(None)
    #print(output)
    #playsound.playsound('1.mp3')
    os.remove(file)


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    respond(location)
    respond(time)
    respond(info)
    respond(weather + "°Celcius")
# voice will convert in to text
def talk():

    print("Listening...")
    input = sr.Recognizer()
    with sr.Microphone() as source:
        input.adjust_for_ambient_noise(source)
        audio = input.listen(source)
        data = ""
        try:
            print("Recognizing..")
            data = input.recognize_google(audio)
            print("User Said...->" + data)
        except sr.UnknownValueError:
            print("Sorry I did not hear your words, Please repeat again.")
    return data


#main function
if __name__ == '__main__':
    wishMe()
    counter =0

    while (1):
        hour = int(datetime.datetime.now().hour)
        if(hour == 10 or hour == 12 or hour == 18 or hour ==22):
            counter = counter+1
            if(counter<3):
                notification.notify(
                        title="** Please Drink Water Now!!",
                        message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
                        # app_icon = "path to your .ico file",
                        timeout=5
                    )
        respond("How can I help you?")
        text = talk().lower()
        #--->print(text)
        # if nothing will said
        if text == "":
            respond("Sorry I did not hear your words, Please repeat again.")
            continue

        if 'wait' in text:
            time.sleep(20)

        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Ok bye and take care")
            break

        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            respond(results)
            print(results)

        elif 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            respond("Google is open")
            time.sleep(5)

        elif ("open word" in text) or ("open microsoft word" in text):
            respond("Opening Microsoft Word")
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word')
            time.sleep(5)

        elif ("open excel" in text) or ("open microsoft excel" in text) :
            respond("Opening Microsoft Excel")
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Excel')
            time.sleep(5)
        elif "open notepad" in text:
            respond("Opening Notepad")
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad')
            time.sleep(5)

        elif 'the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"Sir, the time is {strTime}")

        elif 'how are you' in text:
            respond("I am fine, Thank you")
            respond("How are you")
            text = talk().lower()
            if 'fine' in text or "good" in text:
                respond("It's good to know that you are fine")
            else:
                respond("ok")

        elif "who made you" in text or "who created you" in text:
            respond("I have been created by Tanzeem Khan")

        elif "who are you" in text:
            respond("I am your virtual assistant created by Tanzeem Khan")

        elif 'reason for you' in text or 'why are you created' in text:
            respond("I was created as a Major project by Tanzeem Khan ")

        elif "where is" in text:
            text = text.replace("where is", "")
            location = text
            respond("User asked to Locate")
            respond(location)
            webbrowser.open("https://www.google.nl/maps/place/"+location +"")
            respond("Here is your result")
            time.sleep(10)

        elif 'i love you' in text:
            respond(" I love you too but as a machine")
            respond("It is 7th sense that destroy all other senses")

        elif 'is love' in text:
            respond("It is 7th sense that destroy all other senses")

        elif "write a note" in text:
            respond("What should i write, sir")
            note =talk().lower()
            file = open('jarvis.txt', 'w')
            respond("Sir, Should i include date and time")
            snfm = talk().lower()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m-%d-%Y %T:%M%p")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            respond("this is what you said me to write")
            file = open("C:/Users/Lenovo/PycharmProjects/voice_assis/jarvis.txt", "r")
            print(file.read())
            os.startfile(os.path.join("C:Users/Lenovo/PycharmProjects/voice_assis/jarvis.txt"))
            #file1 = file.read(6)
            #respond(file1)

        elif 'play music' in text or "play a song" in text:
            respond("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "E:/Songs/hindi"
            songs = os.listdir(music_dir)
            #print(songs)
            print(random.choice(songs))
            random1 = os.startfile(os.path.join(music_dir, random.choice(songs)))
            break

        elif 'joke' in text:
            respond(pyjokes.get_joke(language='en', category='all'))

        elif 'lock window' in text:
            respond("locking the device bye bye take care")
            cmd = 'rundll32.exe user32.dll, LockWorkStation'
            subprocess.call(cmd)
            break
            #ctypes.windll.user32.LockWorkStation()

        elif 'shut down' in text:
            respond("Are you sure you want to shut down your computer")
            a = talk().lower()
            if (a =='yes'):
                os.system("shutdown /s /t 1")
            else:
                continue

        elif 'mail' in text:
            respond("Do you want to send mail from your email id of Tanzeem Khan")
            t = talk().lower()
            if(t == "yes"):
                from1 ="khantanzeem.1998@gmail.com"
                pwd ="**********"
                try:
                    respond("What should I say?")
                    content = talk().lower()
                    respond("this is what you said")
                    respond(content)
                    respond("If you want to change it please say yes to type")
                    t=talk().lower()
                    if(t=='yes'):
                        content = input("please type->:  ")

                    respond("whome should i send please type email address")
                    to = input("please type->:  ")
                    #sendEmail(to, content)
                    respond("Email has been sent !")
                except Exception as e:
                    print(e)
                    respond("I am not able to send this email")
            else:
                respond("please type email address")
                from1 = input("please type->:  ")
                respond("please type password of your email address")
                pwd = input("please type->:  ")
                respond("What should I say?")
                content = talk().lower()
                respond("this is what you said")
                respond(content)
                respond("If you want to change it please say yes to type")
                t = talk().lower()
                if (t == 'yes'):
                    content = input("please type->:  ")
                respond("whome should i send please type email address")
                to = input("please type->:  ")
                #sendEmail(to, content)


            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()

            # Enable low security in gmail
            server.login(from1, pwd)
            server.sendmail(from1, to, content)
            server.close()

        elif 'empty recycle bin' in text:
            #winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            respond("Recycle Bin Recycled")

        elif "camera" in text or "take a photo" in text:
            import cv2
            respond("Press Space bar to capture the Image and press Escape to close Camera")
            cam = cv2.VideoCapture(0)
            #cv2.namedWindow("Chitti Camera")
            img_counter = 0
            while True:
                ret, frame = cam.read()
                if not ret:
                    print("failed to grab frame")
                    break
                cv2.imshow("test", frame)
                k = cv2.waitKey(1)
                if k % 256 == 27:
                    # ESC pressed
                    print("Escape hit, closing...")
                    break
                elif k % 256 == 32:
                    # SPACE pressed
                    img_name = "images/pic{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{}".format(img_name))
                    img_counter += 1
            cam.release()
            cv2.destroyAllWindows()

        elif 'weather' in text:
            respond("Say City Name")
            city = talk().lower()
            city = city + " weather"
            weather(city)
            respond("Have a Nice Day:")

        elif 'google' in text:
            respond("Say what do you want to search in google")
            query = talk().lower()
            webbrowser.open_new_tab("https://www.google.com/search?q="+query)

        elif 'youtube' in text:
            respond("Say what do you want to search in Youtube")
            query = talk().lower()
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query="+query)


        elif 'smart' in text:
            fun()
        else:
            respond("Sorry Application is not available right now. i will add this feature in my next version")

