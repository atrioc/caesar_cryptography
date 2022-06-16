import streamlit as st

st.set_page_config(
    page_title="Caesar Cipher",
    page_icon="🔎",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"Get Help": None, "Report a bug": None, "About": None},
)


def encode(text: str, shift):
    """
    shift each character of a string by a given shift value.

    Args
    ----
    text (str):
        The string to encode.
    shift (int):
        The number of bits to shift.

    Returns:
        str: The encoded string

    Raises:
        TypeError: If the shift is not an integer or List of integers.
    """
    # string = text.upper()
    encoded = ""
    if isinstance(shift, int):
        for i in text:
            encoded += chr(ord(i) + shift)
        return encoded
    raise TypeError("shift must be an integer.")


st.title("Encode")
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

# st.write(str(text))
shift_by = st.number_input(
    label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
)

if st.button("encode"):
    if len(text.strip()) > 0:
        st.info(encode(text, shift_by))
    else:
        st.error("No text to encode.")
