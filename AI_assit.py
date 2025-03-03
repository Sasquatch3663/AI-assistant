from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
from langdetect import detect
from serpapi import GoogleSearch
import os

API_KEY = "12a0690a23d8d09af0c65223f0da3def0791295378c4e7897c0cfe5d6ba1bda2"

app = Flask(__name__)

CORS(app)

def transcribe_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "Could not request results from Google Speech Recognition service"

def text_to_speech(text, voice_gender='female'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

def search_online(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "API_KEY"  # Use environment variable for API key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if results.get("organic_results"):
        return results["organic_results"][0]["snippet"]
    return "No results found."

@app.route('/transcribe', methods=['POST'])
def transcribe():
    user_query = transcribe_audio()
    return jsonify({"query": user_query})

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get("query")
    response = search_online(query)
    return jsonify({"response": response})

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text")
    text_to_speech(text)
    return jsonify({"message": "Text has been spoken."})

from waitress import serve

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)
