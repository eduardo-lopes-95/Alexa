import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit
from gtts import gTTS
from playsound import playsound

listener = sr.Recognizer()
engine = pyttsx3.init()

def get_text():
    text = ""
    try:
        with sr.Microphone() as source:
            setupSpeech()
            audio = listener.listen(source)
            text = listener.recognize_google(audio, language='pt-BR')
            print(text)
    except:
        print('Error')

    return text

def setupSpeech():
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say("Diga alguma coisa")
    engine.runAndWait()


def speech(text):
    print(text)
    language = "pt-BR"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sound/output.mp3")
    playsound("./sound/output.mp3")

if __name__ == '__main__':
    #pywhatkit.search(get_text())
    speech(get_text())