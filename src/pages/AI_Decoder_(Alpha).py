# AI for decoding caesar cipher text using NLP
import streamlit as st
import pandas as pd


def makes_sense(text: str):
    """tells whether the given string makes sense"""
    for word in text.split():
        data = pd.read_csv("./data/words.csv")["words"]
        if word.lower() in data.values and word.isalpha():
            return True
    return False


def decoder(text: str):
    shift = 0
    while True:
        # positive shift
        decoded = ""
        for char in text:
            de_char = chr(ord(char) + shift)
            decoded += de_char
        if makes_sense(decoded):
            return decoded

        # Negative shift
        decoded = ""
        for char in text:
            de_char = chr(ord(char) - shift)
            decoded += de_char
        if makes_sense(decoded):
            return decoded

        shift += 1


st.title("AI Decoder")
st.error(
    "This is a beta version of the AI Decoder. It is not ready for production use. It only supports english for now"
)

input_type = st.selectbox(
    label="Select input type",
    options=["Text", "File"],
    help="Select your input type (i.e. text or file).",
)

if input_type == "Text":
    text = st.text_input("Enter text:", help="The text to encode.")
else:
    file = st.file_uploader(label="Upload a file:", help="The file to encode.")
    if file is not None:
        text = file.getvalue().decode("utf-8")


if st.button("decode"):
    st.success(decoder(text))
