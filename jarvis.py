import sys
import os
import pyttsx3 
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import random
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')  
import vlc 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(value=voices[0].id, name=voices[0].id) 
# Media player
media_player = vlc.MediaPlayer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hrs = int(datetime.datetime.now().hour)
    if hrs>=0 and hrs<12:
        speak("Good morning!")
    elif hrs>=12 and hrs<18:
        speak("Good afternoon!")
        
    else:
        speak("Good evening Sir!")       
    speak("Hi i am Jarvis, How may I help you.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      r.pause_threshold = 1
      r.adjust_for_ambient_noise(source)
      audio = r.listen(source)
    try:
      print("Recognizing...")
      query = r.recognize_google(audio, language="en_in")
      print(f"User said : {query}\n")
    except Exception as e :
        print(e)
        print("Try again...")
        return "None"

    return query
     
if __name__ == "__main__":
    wishMe()

     # Logic execution
    while True:
        query = takeCommand().lower() # type: ignore
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, 2)
            speak("As per wikipedia...")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            # browsers.launch("chrome")
            webbrowser.open('google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query or 'play next song' in query or 'play any song' in query or 'play song' in query: 
            music_dir = 'C:\\Sumit\\MUSIC'
            songs = os.listdir(music_dir)
            random_song = random.randint(0, len(songs)-1)
            # os.startfile(os.path.join(music_dir, songs[random_song]))
            media = vlc.Media(os.path.join(music_dir, songs[random_song]))
            media_player.set_media(media)
            media_player.play()
        elif 'stop music' in query:
            media_player.stop()

        elif 'stop jarvis' in query:
            speak('Bye Sir...')
            print('Jarvis stopped')
            sys.exit()
        elif 'the time' in query:
            curr_time = datetime.datetime.now().strftime('%H:%M:S')
            speak(f'Sir, the time is {curr_time}')
        elif 'open vs code' in query:
            vsc_path = 'C:\\Users\\Sumit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(vsc_path)
        elif 'open android studio' in query:
            android_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio'
            os.startfile(android_path)


   

