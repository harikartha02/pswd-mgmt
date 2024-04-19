import streamlit as st
import csv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os
import pandas as pd

# Function to generate AES key
def generate_aes_key():
    aeskey = get_random_bytes(16)  # 16 bytes key for AES-128
    return aeskey

# Function to encrypt password using AES
def encrypt_password(password, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(password.encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    encoded_key = base64.b64encode(key).decode('utf-8')  # Encode the key to base64
    return iv, ct, encoded_key




# Function to write data to CSV file
def write_to_csv(data):
    file_path = os.path.join(os.getcwd(), 'passwords.csv')  # Relative path to passwords.csv
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)




# Streamlit UI
st.title("Password Manager")



username = st.text_input("Enter your username:")
password = st.text_input("Enter your password:", type="password")
website = st.text_input("Enter the website:")

key = None  # Initialize key variable

if st.button("Save Password"):
    if username and password and website:
        key = generate_aes_key()  # Generate AES key for encryption
        iv, encrypted_password, encoded_key = encrypt_password(password, key)  # Note the added variable here
        data = [username, encrypted_password, website, iv, encoded_key]
        write_to_csv(data)
        st.success("Password saved successfully!")
    else:
        st.error("Please fill in all the fields.")



