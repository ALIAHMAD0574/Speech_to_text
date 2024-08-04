# pip install streamlit SpeechRecognition gtts pydub pyttsx3 pyaudio

# please must install ffmpeg  and set its path in the environment variables

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import pyttsx3
import tempfile

# Initialize the recognizer
recognizer = sr.Recognizer()


def recognize_speech_from_mic():
    with sr.Microphone() as source:
        st.write("Listening...")
        # audio = recognizer.listen(source)
        # recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source,phrase_time_limit=20)
        st.write("Processing...")
        try:
            text = recognizer.recognize_google(audio, language="ur-PK")
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Could not request results; check your network connection."


def text_to_speech(text, lang="ur"):
    tts = gTTS(text=text, lang=lang)
    return tts


def main():
    st.title("Urdu Voice Input and Output Application")

    st.write("Press the button and start speaking in Urdu.")

    if st.button("Record Voice"):
        input_text = recognize_speech_from_mic()
        # st.write(f"Recognized Text: {input_text}")
        st.write(f"**Recognized Text: {input_text}**")

        if input_text:
            # Generate a response (echoing input for simplicity)
            response_text = input_text

            # Convert the response text to speech
            tts = text_to_speech(response_text, lang="ur")

            # Save the audio to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            tts.save(temp_file.name)

            # Play the audio file
            st.audio(temp_file.name, format='audio/mp3')

            # Clean up
            temp_file.close()


if __name__ == "__main__":
    main()


# import streamlit as st
# import speech_recognition as sr
# from gtts import gTTS
# import tempfile
# from googletrans import Translator

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Initialize the translator
# translator = Translator()

# def recognize_speech_from_mic():
#     with sr.Microphone() as source:
#         st.write("Listening for 10 seconds...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source, timeout=10)  # Listen for 10 seconds
#         st.write("Processing...")
#         try:
#             text = recognizer.recognize_google(audio, language="ur-PK")
#             return text
#         except sr.UnknownValueError:
#             return "Sorry, I did not understand that."
#         except sr.RequestError:
#             return "Could not request results; check your network connection."

# def text_to_speech(text, lang="ur"):
#     tts = gTTS(text=text, lang=lang)
#     return tts

# def main():
#     st.title("Urdu Voice Input and Translation Application")

#     st.write("Press the button and start speaking in Urdu for up to 10 seconds.")

#     if st.button("Record Voice"):
#         input_text = recognize_speech_from_mic()
#         st.write(f"Recognized Text: {input_text}")

#         if input_text and "Sorry" not in input_text:
#             # Translate the recognized text to English
#             translated_text = translator.translate(input_text, src='ur', dest='en').text
#             st.write(f"Translated Text: {translated_text}")

#             # Convert the response text to speech in Urdu (or any other language as needed)
#             tts = text_to_speech(translated_text, lang="en")

#             # Save the audio to a temporary file
#             temp_file = tempfile.NamedTemporaryFile(delete=False)
#             tts.save(temp_file.name)

#             # Play the audio file
#             st.audio(temp_file.name, format='audio/mp3')

#             # Clean up
#             temp_file.close()

# if __name__ == "__main__":
#     main()
