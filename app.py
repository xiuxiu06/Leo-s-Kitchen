import streamlit as st

st.set_page_config(page_title="Leo's Food App", page_icon="🐱", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
st.sidebar.page_link("app.py", label="🏠 Home", icon="🏠")
st.sidebar.page_link("pages/about_me.py", label="ℹ️ About Me")
st.sidebar.page_link("pages/my_recipes.py", label="📊 My Recipes")
st.sidebar.page_link("pages/chatbot.py", label="🤖 Chat Bot")

st.title("Welcome to Leo's Food App! 🐱🍽️")
st.write("Navigate using the sidebar to explore recipes, chatbot, and more.")
