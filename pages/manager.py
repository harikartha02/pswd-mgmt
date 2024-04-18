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

def decrypt_password(iv, ct, encoded_key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    key = base64.b64decode(encoded_key)  # Decode the key from base64
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt


# Function to write data to CSV file
def write_to_csv(data):
    file_path = os.path.join(os.getcwd(), 'passwords.csv')  # Relative path to passwords.csv
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Function to read data from CSV file
def read_from_csv():
    try:
        file_path = os.path.join(os.getcwd(), 'passwords.csv')
        df = pd.read_csv(file_path, header=None, usecols=[0, 1, 2, 3, 4], names=['Username', 'Encrypted_Password', 'Website', 'IV', 'encoded_key'])
        return df
    except FileNotFoundError:
        return None


# Streamlit UI
st.title("Password Manager")

admin_password = "admin"  # Pre-defined administrator password

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


show_passwords = False
admin_password_entered = st.text_input("Enter administrator password:", type="password")
if admin_password_entered == admin_password:
    show_passwords = st.button("Show Passwords")

if show_passwords:
    st.write("## Saved Passwords")
    df = read_from_csv()
    if df is not None:
        if not df.empty:
            # Make sure to change 'Key' to 'encoded_key' or whichever name you've used for the base64 encoded key
            df['Decrypted_Password'] = df.apply(lambda row: decrypt_password(row['IV'], row['Encrypted_Password'], row['encoded_key']), axis=1)
            disp = df[['Website', 'Username', 'Decrypted_Password']]
            st.dataframe(disp, width=700)
        else:
            st.write("No passwords saved yet.")
    else:
        st.error("No data read from CSV.")

