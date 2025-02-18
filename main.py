import speech_recognition as sr
import pyttsx3
from Agents import agent, llm
import re


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    try:
        action_words = ["open", "find", "search"]
        if any(word in c.lower() for word in action_words):
            # Use agent for action-based commands
            response = agent.run(c)
            speak("Finished Processing the request, Is there anything else I can help you with, sir?")
        else:
            # Use the same Ollama LLM instance for general questions
            response = llm.invoke(
                f"""As Jarvis, respond to: {c}
                Remember to be:
                - short, concise, human like and direct in your responses without crossquentionaing the user
                """
            )
            speak(response)
        
    except Exception as e:
        print(f"Error: {str(e)}")  # Print the actual error for debugging
        speak("I encountered an error while processing your request. Please try again, sir.")
    


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
                speak("  Yes Sir  ")
                #listen for command now 
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    # Check for termination command
                    if command.lower() == "terminate":
                        speak("Shutting down. Goodbye sir.")
                        break


                    processCommand(command)


         
        
        except Exception as e:
            print("Error {0}".format(e))



