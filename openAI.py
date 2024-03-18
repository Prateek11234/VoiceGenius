import speech_recognition as sr
import os
import webbrowser

def say(text):
    os.system(f"say {text}")

def ordertake():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  1
        audio = r.listen(source)
        try:
            print("recognizing")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "okay sorry!! coud not recognize. please speak once agin"

        
        
if __name__ == '__main__' :
    print('PyCharm')
    say("hey myself name ,Tell me how can i help you ")
    while True:
        print("listening..........")
        query = ordertake()
        sites = [["facebook","https://facebook.com"],["instagram","https://instagram.com"],["youtube","https://youtube.com"]["google","https://google.com"]]   #and much more sites can be added..
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} ...")
                webbrowser.open(site[1])    
