# import streamlit as st
# import pyttsx3

# def initialize_engine():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     return engine, voices

# def speak_text(text, voice_id, rate):
#     engine, voices = initialize_engine()
#     engine.setProperty('voice', voices[voice_id].id)
#     engine.setProperty('rate', rate)
#     engine.say(text)
#     engine.runAndWait()

# def main():
#     st.set_page_config(page_title='Text to Speech App', layout='wide')
    
#     st.markdown("""
#         <style>
#         .main-container {
#             text-align: center;
#             font-family: Arial, sans-serif;
#         }
#         .stTextArea textarea {
#             font-size: 18px;
#         }
#         .stButton button {
#             background-color: #007BFF;
#             color: white;
#             font-size: 18px;
#             padding: 10px;
#             border-radius: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True)
    
#     st.title("🔊 Text-to-Speech App")
#     st.subheader("Convert your text into speech using different male voices")
    
#     text_input = st.text_area("Enter text to convert to speech:", "Hello, welcome to the Text-to-Speech app!")
    
#     engine, voices = initialize_engine()
    
#     # Filter and select 5 different male voices
#     male_voices = [v for v in voices if 'male' in v.name.lower() or 'david' in v.name.lower() or 'microsoft' in v.name.lower()]
#     male_voices = male_voices[:5] if len(male_voices) >= 5 else male_voices
    
#     voice_options = {i: male_voices[i].id for i in range(len(male_voices))}
    
#     selected_voice = st.selectbox("Select Male Voice:", list(voice_options.keys()), format_func=lambda x: male_voices[x].name)
    
#     rate = st.slider("Adjust Speech Rate:", 100, 250, 150)
    
#     if st.button("Convert to Speech"):
#         if text_input.strip() != "":
#             speak_text(text_input, selected_voice, rate)
#             st.success("Speech played successfully!")
#         else:
#             st.warning("Please enter some text!")

# if __name__ == "__main__":
#     main()















# import streamlit as st
# import pyttsx3

# def initialize_engine():
#     engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     return engine, voices

# def speak_text(text, voice_id, rate):
#     engine, voices = initialize_engine()
#     engine.setProperty('voice', voices[voice_id].id)
#     engine.setProperty('rate', rate)
#     engine.say(text)
#     engine.runAndWait()

# def main():
#     st.set_page_config(page_title='Text to Speech App', layout='wide')
    
#     st.markdown("""
#         <style>
#         .main-container {
#             text-align: center;
#             font-family: Arial, sans-serif;
#         }
#         .stTextArea textarea {
#             font-size: 18px;
#         }
#         .stButton button {
#             background-color: #007BFF;
#             color: white;
#             font-size: 18px;
#             padding: 10px;
#             border-radius: 10px;
#         }
#         </style>
#         """, unsafe_allow_html=True)
    
#     st.title("🔊 Text-to-Speech App")
#     st.subheader("Convert your text into speech using different male voices")
    
#     text_input = st.text_area("Enter text to convert to speech:", "Hello, welcome to the Text-to-Speech app!")
    
#     engine, voices = initialize_engine()
    
#     # Filter and select more male voices
#     male_voices = [v for v in voices if 'male' in v.name.lower() or 'david' in v.name.lower() or 'microsoft' in v.name.lower()]
#     male_voices = male_voices[:10] if len(male_voices) >= 10 else male_voices  # Increase to 10 voices if available
    
#     voice_options = {i: male_voices[i].id for i in range(len(male_voices))}
    
#     selected_voice = st.selectbox("Select Male Voice:", list(voice_options.keys()), format_func=lambda x: male_voices[x].name)
    
#     rate = st.slider("Adjust Speech Rate:", 100, 250, 150)
    
#     if st.button("Convert to Speech"):
#         if text_input.strip() != "":
#             speak_text(text_input, selected_voice, rate)
#             st.success("Speech played successfully!")
#         else:
#             st.warning("Please enter some text!")

# if __name__ == "__main__":
#     main()



                 
























# import streamlit as st
# from gtts import gTTS

# # Streamlit App Title
# st.title("🗣️ Male Voice Text-to-Speech App")

# # User Input
# text = st.text_area("Enter text to convert into speech:", "Hello! This is a male voice speaking.")

# # Convert Text to Speech
# if st.button("Generate Speech"):
#     if text.strip() == "":
#         st.warning("Please enter some text.")
#     else:
#         # Generate Male Voice Speech (UK English Male Voice)
#         tts = gTTS(text=text, lang="en", tld="co.uk")  # "co.uk" domain gives a deeper male-like voice
#         tts.save("male_voice.mp3")

#         # Play Audio
#         st.audio("male_voice.mp3", format="audio/mp3")

#         # Success Message
#         st.success("✅ Male voice speech generated successfully!")
import streamlit as st
from gtts import gTTS

# Streamlit App Title
st.title("🗣️ Male Voice Text-to-Speech App")

# User Input
text = st.text_area("Enter text to convert into speech:", "Hello! This is a male voice speaking.")

# Convert Text to Speech
if st.button("Generate Speech"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Generate Male Voice Speech (UK English Male Voice)
        tts = gTTS(text=text, lang="en", tld="co.uk")  # "co.uk" domain gives a deeper male-like voice
        audio_file = "male_voice.mp3"
        tts.save(audio_file)

        # Play Audio
        st.audio(audio_file, format="audio/mp3")

        # Provide Download Option
        with open(audio_file, "rb") as file:
            st.download_button(
                label="📥 Download Speech",
                data=file,
                file_name="male_voice.mp3",
                mime="audio/mp3"
            )
        
        # Success Message
        st.success("✅ Male voice speech generated successfully!")
