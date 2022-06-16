import streamlit as st

st.title("Decode")


def decode(text: str, shift: int):
    """
    decode each character of a string by a given shift value.

    Args
    ----
    text (str):
        The string to decode.
    shift (int):
        The number by which characters are shifted.

    Returns:
        str: The decoded string
    """
    decoded = ""
    if isinstance(shift, int):
        for i in text:
            decoded += chr(ord(i) - shift)
        return decoded
    raise TypeError("shift must be an integer.")


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

shift = st.number_input(
    label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
)

if st.button("decode"):
    if len(text.strip()) > 0:
        st.info(decode(text, shift))
    else:
        st.error("No text to decode.")
