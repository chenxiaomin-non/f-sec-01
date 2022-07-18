import streamlit as st
import time

def ceasar(cipher: str, key: int):
    char_A = ord('A')
    list_cipher = []
    
    with st.spinner("\nStarting to encrypt/decrypt...\n"):
        time.sleep(1)
             
    for i in cipher:
        
        if i.isalpha() is False:
            st.write(i + " -> " + i)
            list_cipher.append(i)
            continue
        
        value = (ord(i) - char_A + key) % 26 + char_A
        st.write(i + " + " + str(key) + " -> " + chr(value))
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

    
def goldbug(plaintext: str):
    list_char = ['!', '@', '#', 'a', 'b', '1', '&', '$', '%', '^', 
                 '*', '(', ')', '-', '2', '3', '4', '_', '=', '+',
                 ':', ';', '{', '}', '|', '\\', '>', '<']
    result = ""
    freq = {}
    for char in plaintext:
        freq[char] = freq.get(char, 0) + 1
        index = ord(char) - ord('A')
        result += list_char[index]
    st.write("Analyze frequency of the text")
    for k,v in freq.items():
        st.write('Character: %s -> %s times' %(k, v,))
    return result
        
st.header("3. Goldbug Cipher")
st.write("Enter ciphertext you want to decrypt or plaintext you want to encrypt:")

cipher_g = st.text_input("Goldbug C/P: ")

if st.button("Goldbug!!!"):
    cipher = goldbug(cipher_g.upper())
    st.write("Your ciphertext is: " + cipher)
    
