import streamlit as st

st.title("decrypt")


def decrypt(text: str, shift: int):
    """
    decrypt each character of a string by a given shift value.

    Args
    ----
    text (str):
        The string to decrypt.
    shift (int):
        The number by which characters are shifted.

    Returns:
        str: The decrypted string
    """
    decrypted = ""
    if isinstance(shift, int):
        for i in text:
            decrypted += chr(ord(i) - shift)
        return decrypted
    raise TypeError("shift must be an integer.")


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

shift = st.number_input(
    label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
)

if st.button("decrypt"):
    if len(text.strip()) > 0:
        st.info(decrypt(text, shift))
    else:
        st.error("No text to decrypt.")
