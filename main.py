import speech_recognition as sr
import pyttsx3
from Agents import agent


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    try:
        response = agent.run(c)
        speak("Finished processing your request sir, is there anything else I can help you with?")
    except Exception as e:
        speak(f"I encountered an error:")
    


if __name__ == '__main__':
    speak("  Hello sir How can I help you")




    while True:
        #listen for the wake word "Jarvis"
        #Obtaining audio from the microphone

        r = sr.Recognizer()
        


        #recognize speech using google
        try:
            with sr.Microphone() as source:
             print("Listening...")
             audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes Sir")
                #listen for command now 
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)


                    processCommand(command)


         
        
        except Exception as e:
            print("Error {0}".format(e))
        


