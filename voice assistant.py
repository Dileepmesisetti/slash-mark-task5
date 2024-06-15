import speech_recognition
import webbrowser

speech_recognition.Microphone(device_index=1)

r = speech_recognition.Recognizer()

r.energy_threshold = 5000

with speech_recognition.Microphone() as source:
    print("speek somthing to recognige,i'll get you there!...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        url = 'https://www.google.co.in/search?q='
        search_url = url+text
        webbrowser.open(search_url)
    except:
        print("Can't recognize what you are saying!")
        