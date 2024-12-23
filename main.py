import speech_recognition as sr
import webbrowser
import pyttsx3
import google.generativeai as genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        speak("Opening Linkedin")
        webbrowser.open("https://www.linkedin.com")
    else:
        AiprocessCommand(c)
    
def AiprocessCommand(c): #processing the command using AI
    
    genai.configure(api_key="API_Key") # Replace with your Gemini API key
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"You are a virtual assistant and you are designed to help people with their daily tasks and giving short crisp responses with your tone based on the seriousness of question Assume you have been helping and you know me very well also as a rule give response in one time only treating it as a one time conversation dont ask any cross questions or anything just give the response in one time only. So my latest request with you as my assistant is   - {c}")
    speak(response.text)


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
             audio = r.listen(source, timeout=2, phrase_time_limit=1)
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
        


