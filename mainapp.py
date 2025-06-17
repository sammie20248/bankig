import streamlit as st
from homepage import render_home
from auth import login

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.logged_in:
    render_home()
else:
    login()
