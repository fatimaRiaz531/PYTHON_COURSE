import streamlit as st
import datetime

# Page configuration
st.set_page_config(
    page_title="Mindset Growth Tracker",
    page_icon="🌱",
    layout="wide"
)

# Title and description
st.title("🌱 Mindset Growth Tracker")
st.markdown("Apne mindset ko track karein aur positive rahein!")

# Sidebar for navigation
page = st.sidebar.selectbox(
    "Page Selection",
    ["Daily Check-in", "Progress Tracker"]
)

if page == "Daily Check-in":
    st.header("Daily Mindset Check-in")
    
    # Date selector
    today = st.date_input("Date", datetime.datetime.now())
    
    # Mood tracker
    mood = st.slider("Aaj aap kaisa mehsoos kar rahe hain? (1-10)", 1, 10, 5)
    
    # Gratitude section
    gratitude = st.text_area("Aaj aap kis cheez ke liye thankful hain?")
    
    # Goals section
    goal = st.text_input("Aaj ka main goal kya hai?")
    
    # Positive affirmation
    affirmations = [
        "Main har din behtar ho raha/rahi hun",
        "Main apni growth pe focus kar raha/rahi hun",
        "Main challenges ko opportunities ki tarah dekhta/dekhti hun"
    ]
    selected_affirmation = st.selectbox("Aaj ka positive affirmation:", affirmations)
    
    if st.button("Save Entry"):
        st.success("Aaj ka entry save ho gaya!")
        
elif page == "Progress Tracker":
    st.header("Progress Tracker")
    
    # Sample progress metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Weekly Check-ins", value="5")
    
    with col2:
        st.metric(label="Average Mood", value="7.5")
    
    with col3:
        st.metric(label="Goals Completed", value="12")
    
    st.subheader("Tips for Mindset Growth:")
    tips = [
        "Regular meditation karein",
        "Positive logon se connect karein",
        "New skills seekhne ki koshish karein",
        "Gratitude journal maintain karein",
        "Regular exercise karein"
    ]
    
    for tip in tips:
        st.markdown(f"• {tip}") 