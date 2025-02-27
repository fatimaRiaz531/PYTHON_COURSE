import streamlit as st
import time
import random

# Quiz questions (20 Python-related MCQs)
questions = [
    {"question": "What does HTML stand for?", 
     "options": ["Hyper Text Markup Language", "High Text Markup Language", "Hyper Tabular Markup Language", "None of these"], 
     "answer": "Hyper Text Markup Language"},
    {"question": "Which language is used for web development?", 
     "options": ["Python", "Java", "JavaScript", "All of the above"], 
     "answer": "All of the above"},
    {"question": "What does CSS stand for?", 
     "options": ["Cascading Style Sheets", "Colorful Style Sheets", "Computer Style Sheets", "Creative Style Sheets"], 
     "answer": "Cascading Style Sheets"},
    {"question": "What is the correct file extension for Python files?", 
     "options": [".py", ".python", ".pt", ".px"], 
     "answer": ".py"},
    {"question": "What is the output of print(2 + 3 * 5)?", 
     "options": ["25", "17", "10", "None of these"], 
     "answer": "17"},
    {"question": "Which keyword is used to define a function in Python?", 
     "options": ["def", "define", "function", "func"], 
     "answer": "def"},
    {"question": "What is the purpose of the 'pass' statement in Python?", 
     "options": ["To skip an iteration", "To define an empty block", "To exit a loop", "To raise an exception"], 
     "answer": "To define an empty block"},
    {"question": "What is the result of bool('False') in Python?", 
     "options": ["True", "False", "None", "Error"], 
     "answer": "True"},
    {"question": "Which data structure is immutable in Python?", 
     "options": ["List", "Tuple", "Dictionary", "Set"], 
     "answer": "Tuple"},
    {"question": "What is the correct syntax to create an empty set in Python?", 
     "options": ["{}", "set()", "[]", "()"], 
     "answer": "set()"},
]

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = None
if 'show_feedback' not in st.session_state:
    st.session_state.show_feedback = False
if 'feedback_message' not in st.session_state:
    st.session_state.feedback_message = ""
if 'feedback_type' not in st.session_state:
    st.session_state.feedback_type = ""
if 'shuffled_questions' not in st.session_state:  # To store shuffled questions
    st.session_state.shuffled_questions = []

# Title and subtitle
st.title("🎮 Python Quiz Challenge 🌟")
st.subheader("Created by Fatima")

# Get user's name
if st.session_state.user_name is None:
    user_name = st.text_input("Enter your name to start the quiz:")
    if st.button("Start Quiz"):
        if user_name.strip() == "":
            st.error("Please enter your name to proceed. 😔")
        else:
            st.session_state.user_name = user_name
            # Shuffle questions only once per game start
            st.session_state.shuffled_questions = random.sample(questions, len(questions))
            st.rerun()

# Display quiz content only if the user has entered their name
if st.session_state.user_name:
    st.write(f"Welcome, **{st.session_state.user_name}**! Let's begin the quiz. 🚀")
    
    if not st.session_state.game_over:
        # Show feedback if any
        if st.session_state.show_feedback:
            if st.session_state.feedback_type == "success":
                st.balloons()
                st.success(st.session_state.feedback_message)
            elif st.session_state.feedback_type == "error":
                st.error(st.session_state.feedback_message)
            
            # Wait for 2 seconds before moving to the next question
            time.sleep(2)
            st.session_state.show_feedback = False
            st.session_state.current_question += 1
            st.rerun()

        # Check if all questions are answered
        if st.session_state.current_question < len(st.session_state.shuffled_questions):
            question_data = st.session_state.shuffled_questions[st.session_state.current_question]
            st.subheader(f"Question {st.session_state.current_question + 1}: {question_data['question']} ❓")
            
            selected_option = st.radio("Select an answer:", question_data['options'], index=None)
            if st.button("Submit") and selected_option is not None:
                if selected_option == question_data['answer']:
                    st.session_state.score += 1
                    st.session_state.feedback_message = "Good job! ✨🎉"
                    st.session_state.feedback_type = "success"
                else:
                    st.session_state.feedback_message = "Wrong answer! 😔👎"
                    st.session_state.feedback_type = "error"
                
                st.session_state.show_feedback = True
                st.rerun()
        else:
            st.session_state.game_over = True

    # Display final score and feedback when the game is over
    if st.session_state.game_over:
        total_questions = len(st.session_state.shuffled_questions)
        score = st.session_state.score
        percentage = (score / total_questions) * 100
        
        # Provide feedback based on performance
        if percentage >= 80:
            feedback = f"{st.session_state.user_name}, you did amazing! 🎉 Keep shining!"
        elif percentage >= 50:
            feedback = f"{st.session_state.user_name}, good effort! 💪 Try again to improve."
        else:
            feedback = f"{st.session_state.user_name}, keep practicing! 🌱 You'll get better with time."
        
        # Display final score and feedback
        st.error(f"Game Over 😢 {st.session_state.user_name}, you scored {score}/{total_questions}.")
        st.info(feedback)
        
        # Exit button
        if st.button("Exit Quiz"):
            st.write(f"Thank you for playing, {st.session_state.user_name}! 👋😄")
            st.write("Created by Fatima ❤️")
            st.stop()
        
        # Restart button
        if st.button("Restart Quiz"):
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.game_over = False
            st.session_state.user_name = None
            st.session_state.show_feedback = False
            st.session_state.feedback_message = ""
            st.session_state.feedback_type = ""
            st.session_state.shuffled_questions = []  # Clear shuffled questions
            st.rerun()