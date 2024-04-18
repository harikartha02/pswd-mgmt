import streamlit as st
import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def check_password_strength(password):
    n_upper = sum(1 for c in password if c.isupper())
    n_lower = sum(1 for c in password if c.islower())
    n_digits = sum(1 for c in password if c.isdigit())
    n_symbols = sum(1 for c in password if c in string.punctuation)
    length = len(password)

    criteria = [
        length >= 8,
        n_upper > 0,
        n_lower > 0,
        n_digits > 0,
        n_symbols > 0
    ]

    strength = sum(criteria)
    strength_label = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    return strength_label[strength-1]

st.title("Password Generator and Strength Checker")

# Password generation settings
st.header("Generate a New Password")

length = st.slider("Length", min_value=6, max_value=20, value=12, key="length")
col1, col2, col3= st.columns(3)
use_uppercase = col1.checkbox("Uppercase", value=True, key="uppercase")
use_numbers = col2.checkbox("Numbers", value=True, key="numbers")
use_symbols = col3.checkbox("Symbols", value=True, key="symbols")

if st.button("Generate Password"):
    generated_password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    st.text_input("Generated Password", generated_password, key="gen_pass")
    password_strength = check_password_strength(generated_password)
    st.write(f"Strength: {password_strength}")

# Password strength check
st.header("Check Existing Password Strength")
user_password = st.text_input("Enter a password to check strength", key="user_password")
if user_password:
    strength = check_password_strength(user_password)
    st.write(f"Strength: {strength}")
