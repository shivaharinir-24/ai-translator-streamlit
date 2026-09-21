import streamlit as st
from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🌍 AI Language Translator")
languages = ["English", "Tamil", "Hindi", "French", "German", "Spanish"]
source_language = st.selectbox("Select Source Language", languages)
target_language = st.selectbox("Select Target Language", languages)
text_to_translate = st.text_area("Enter text to translate")
if st.button("Translate"):
    if not text_to_translate:
        st.warning("Please enter text to translate.")
    else:
        st.write(f"Translating from {source_language} to {target_language}...")
        prompt = f"Translate the following text from {source_language} to {target_language}: {text_to_translate}"
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )
        translated_text = response.output_text
        st.success("Translation completed!")
        st.write(f"Translated Text: {translated_text}")

