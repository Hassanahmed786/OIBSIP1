import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Say that again please...")
        return None
    return command.lower()

def respond_to_hello():
    speak("Hello! How can I assist you today?")

def tell_time():
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    speak(f"The current time is {time}")

def tell_date():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    speak(f"Today's date is {date}")

def search_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

def main():
    while True:
        command = take_command()
        if command:
            if 'hello' in command:
                respond_to_hello()
            elif 'time' in command:
                tell_time()
            elif 'date' in command:
                tell_date()
            elif 'search' in command:
                query = command.replace("search", "")
                search_wikipedia(query)
            elif 'stop' in command:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    speak("Initializing voice assistant")
    main()
