# Robo-Voice-Translation

This Python script is designed to capture spoken English input from a user, translate the recognized text into Hindi, and play back the translated text as speech. It utilizes several libraries to handle speech recognition, translation, and text-to-speech conversion.

# Features
Speech Recognition: Converts spoken English to text using Google's Speech Recognition API.
Text Translation: Translates the recognized English text into Hindi using the googletrans library.
Text-to-Speech: Converts the translated Hindi text into speech and plays it using Google's Text-to-Speech (gTTS) service.

# Requirements
To run this script, you'll need to have the following Python libraries installed:

SpeechRecognition: For capturing and recognizing spoken words.
gTTS: Google Text-to-Speech for converting text into speech.
googletrans==4.0.0-rc1: For translating text between languages.
pyaudio: For accessing microphone input.
playsound: For playing audio files.
# You can install the necessary libraries using pip:
pip install SpeechRecognition gTTS googletrans==4.0.0-rc1 playsound pyaudio
