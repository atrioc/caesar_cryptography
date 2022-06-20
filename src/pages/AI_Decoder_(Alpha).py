import streamlit as st
import pandas as pd


def makes_sense(text: str):
    """tells whether the given string makes sense"""
    for word in text.strip().split():
        data = pd.read_csv("./data/words.csv")["words"]
        if all([word.isalpha(), word.lower() in data.values, len(word) > 2]):
            return True
    return False


def decrypt(text: str):
    """
    decryptr decryptd the caesar cipher

    Parameters
    ----------
    text : str
        The text to be decrypted.

    Returns
    -------
    str
        The decrypted text.
    """
    shift = 0
    while True:
        # Positive shift
        decrypted = ""
        for char in text:
            decrypted += chr(ord(char) + shift)
        if makes_sense(decrypted):
            return decrypted

        # Negative shift
        decrypted = ""
        for char in text:
            decrypted += chr(ord(char) - shift)
        if makes_sense(decrypted):
            return decrypted

        shift += 1


st.title("AI decryptor")
st.error(
    "This is a beta version of the AI decryptor. It is not ready for production use. It only supports english decoding for now"
)

input_type = st.selectbox(
    label="Select input type",
    options=["Text", "File"],
    help="Select your input type (i.e. text or file).",
)

if input_type == "Text":
    text = st.text_input("Enter text:", help="The text to encrypt.")
else:
    file = st.file_uploader(label="Upload a file:", help="The file to encrypt.")
    if file is not None:
        text = file.getvalue().decrypt("utf-8")


if st.button("decrypt"):
    if len(text.strip()) > 0:
        st.success(decryptor(text))
    else:
        st.error("No text to encrypt.")
