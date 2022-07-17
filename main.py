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
st.header("1. Ceasar Cipher:")
st.write("Enter ciphertext you want to decrypt or plaintext you want to encrypt:")

cipher = st.text_input("Ciphertext/Plaintext: ")
key = st.slider("Key: ", 0, 25, 0)

if st.button("Decrypt/Encrypt"):
    plaintext = ceasar(cipher.upper(), key)
    st.write("Your ciphertext/plaintext is: " + plaintext)

    
def vigenere(cipher: str, key: str):
    char_A = ord('A')
    result = ""
    for i in range(len(cipher)):
        if cipher[i].isalpha() is False:
            result += cipher[i]
            continue
        value = ord(cipher[i]) - char_A
        mini_key = ord(key[i%len(key)]) - char_A
        value = (value + mini_key) % 26 + char_A
        result += chr(value)
    return result
 
st.header("2. Vigenere Cipher")
st.write("Enter ciphertext you want to decrypt or plaintext you want to encrypt:")

cipher_v = st.text_input("Vigenere Ciphertext/Plaintext: ")
key_v = st.text_input("Vigenere Key: ")

if st.button(" Decrypt/Encrypt "):
    plaintext = vigenere(cipher_v.upper(), key_v.upper())
    st.write("Your ciphertext/plaintext is: " + plaintext)
