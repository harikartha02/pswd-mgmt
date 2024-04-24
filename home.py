import streamlit as st


from Fire import initialize_firebase

# Call initialize_firebase function when needed
#firebase_bucket = initialize_firebase()

# Now you can use the firebase_bucket reference to interact with Firebase Storage




# Page Title and Header
st.title("Password Manager")
st.header("Welcome to our Password Manager App")

# Introduction
st.write("""
         The password manager app helps you securely store and manage your passwords for various websites and services.
         Say goodbye to the hassle of remembering multiple passwords or writing them down on sticky notes!
         """)

# Key Features
st.header("Key Features")
st.write("""
         - Secure Password Storage: Safely store all your passwords in one place.
         - Encryption: Your passwords are encrypted using AES-128 to ensure maximum security.
         - Easy Access: Access your passwords anytime, anywhere, from any device.
         - Cloud Sync: Sync your passwords across multiple devices for seamless access.
         - User-Friendly Interface: Intuitive and easy-to-use interface for a hassle-free experience.
         """)

# Get Started
st.header("Get Started")
st.write("""
         Ready to take control of your passwords? Sign up now and start managing your passwords securely!
         Use the Navigation Bar to test out different features of the project.
         """)


