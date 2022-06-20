import streamlit as st


def encrypt(text: str, shift: int):
    """
    shift each character of a string by a given shift value.

    Args
    ----
    text (str):
        The string to encrypt.
    shift (int):
        The number of bits to shift.

    Returns:
        str: The encrypted string

    Raises:
        TypeError: If the shift is not an integer or List of integers.
    """
    # string = text.upper()
    encrypted = ""
    if isinstance(shift, int):
        for i in text:
            encrypted += chr(ord(i) + shift)
        return encrypted
    raise TypeError("shift must be an integer.")


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


st.title("Example")
input_type = st.selectbox(
    label="Select input type",
    options=["Text", "File"],
    help="Select your input type (i.e. text or file).",
)

if input_type == "Text":
    text = st.text_area("Enter text:", help="The text to encrypt.", height=180)
else:
    file = st.file_uploader(label="Upload a file:", help="The file to encrypt.")
    if file is not None:
        text = file.getvalue().decrypt("utf-8")

# st.write(str(text))
shift_by = st.number_input(
    label="Enter a shift value:", step=1, help="Number of bits to shift each bit with."
)

if st.button("Start..."):
    if text.strip() != "":
        with st.expander("Given Text"):
            st.info(text)

        with st.expander("Encrypted Text"):
            encrypted = encrypt(text, shift_by)
            st.info(encrypted)

        with st.expander("Decrypted Text"):
            decrypted = decrypt(encrypted, shift_by)
            st.info(decrypted)
    else:
        st.error("Please enter text.")
