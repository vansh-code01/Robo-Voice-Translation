import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import playsound
import os

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Please speak something in English...")

        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Capture the audio
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    return None

def translate_text(text, target_language='hi'):
    # Initialize the translator
    translator = Translator()

    # Translate the text to the target language
    translation = translator.translate(text, dest=target_language)
    print(f"Translated Text: {translation.text}")
    return translation.text

def text_to_speech(text, language='hi'):
    # Convert the translated text to speech
    tts = gTTS(text=text, lang=language)

    # Save the converted audio to a file
    filename = "translated_speech.mp3"
    tts.save(filename)

    # Play the audio file
    playsound.playsound(filename)

    # Remove the audio file after playing
    os.remove(filename)

def main():
    # Recognize speech from the user
    recognized_text = recognize_speech()

    if recognized_text:
        # Translate the recognized text from English to Hindi
        translated_text = translate_text(recognized_text, target_language='hi')

        # Convert the translated text to speech and play it
        text_to_speech(translated_text, language='hi')

if __name__ == "__main__":
    main()
