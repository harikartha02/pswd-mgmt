import streamlit as st
import csv
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import os
import pandas as pd

def decrypt_password(iv, ct, encoded_key):
    iv = base64.b64decode(iv)
    ct = base64.b64decode(ct)
    key = base64.b64decode(encoded_key)  # Decode the key from base64
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')
    return pt


# Function to read data from CSV file
def read_from_csv():
    try:
        file_path = os.path.join(os.getcwd(), 'passwords.csv')
        df = pd.read_csv(file_path, header=None, usecols=[0, 1, 2, 3, 4], names=['Username', 'Encrypted_Password', 'Website', 'IV', 'encoded_key'])
        return df
    except FileNotFoundError:
        return None


admin_password = "admin"  # Pre-defined administrator password

st.write("## Saved Passwords")

show_passwords = False
admin_password_entered = st.text_input("Enter administrator password:", type="password")
if admin_password_entered == admin_password:
    show_passwords = st.button("Show Passwords")

if show_passwords:
    
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
