from flask import Flask, request, jsonify
from flask_cors import CORS
import speech_recognition as sr
import pyttsx3
from serpapi import GoogleSearch
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

SERPAPI_KEY = os.getenv("SERPAPI_KEY")  # Use environment variable for security

# Function to transcribe speech to text
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

# Function to convert text to speech
def text_to_speech(text, voice_gender='female'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    if voice_gender == 'female':
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    engine.say(text)
    engine.runAndWait()

# Function to perform an online search using SerpAPI
def search_online(query):
    if not SERPAPI_KEY:
        return "Error: SERPAPI_KEY is missing"

    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY
    }
    
    search = GoogleSearch(params)
    results = search.get_dict()

    if results.get("organic_results"):
        return results["organic_results"][0]["snippet"]
    
    return "No results found."

# Unified API endpoint for transcribe, search, and speak
@app.route('/process', methods=['POST'])
def process_request():
    data = request.json
    action = data.get("action")

    if not action:
        return jsonify({"error": "Please provide an action (transcribe, search, speak)"}), 400

    if action == "transcribe":
        return jsonify({"query": transcribe_audio()})

    elif action == "search":
        query = data.get("query")
        if not query:
            return jsonify({"error": "Please provide a search query"}), 400
        return jsonify({"response": search_online(query)})

    elif action == "speak":
        text = data.get("text")
        if not text:
            return jsonify({"error": "Please provide text to speak"}), 400
        text_to_speech(text)
        return jsonify({"message": "Text has been spoken."})

    else:
        return jsonify({"error": "Invalid action. Use 'transcribe', 'search', or 'speak'"}), 400

from waitress import serve

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)
