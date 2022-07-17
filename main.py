import streamlit as st

def ceasar(cipher: str, key: int):
    char_A = ord('A')
    list_cipher = []
    for i in cipher:
        if i.isalpha() is False:
            list_cipher.append(i)
            continue
        value = (ord(i) - char_A + key) % 26 + char_A
        list_cipher.append(chr(value))
    result = ""
    for i in list_cipher:
        result += i
    
    return result

st.title("Tool for today!")
st.write("Enter ciphertext you want to decrypt or plaintext you want to encrypt:")

cipher = st.text_input("Ciphertext/Plaintext: ")
key = st.slider("Key: ", 0, 25, 0)

if st.button("Decrypt/Encrypt"):
    plaintext = ceasar(cipher.upper(), key)
    st.write("Your ciphertext/plaintext is: " + plaintext)
