#this is my talky which works for me by just giving him a voice command
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random
import requests
import json
import wikipedia
# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()         
            