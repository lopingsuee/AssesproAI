import streamlit as st

def url_input():
    return st.text_input("Tempel link video (YouTube/Drive/Dropbox/Direct):", "")

def upload_input():
    return st.file_uploader("Unggah video (mp4/mov/webm)", type=["mp4","mov","webm"])
