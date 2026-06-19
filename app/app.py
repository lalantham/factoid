import streamlit as st

# Application configuration
st.set_page_config(page_title="Factoid - Trivia Quiz", page_icon="💡", layout="centered")

# Sample Quiz Data
QUIZ_DATA = [
    {
        "question": "Which Linux distribution uses the 'pacman' package manager by default?",
        "options": ["Ubuntu", "Arch Linux", "Fedora", "Debian"],
        "answer": "Arch Linux"
    },
    {
        "question": "What does the 'K' in KDE stand for originally?",
        "options": ["Kool", "Kinetix", "Krypton", "Kernel"],
        "answer": "Kool"
    },
    {
        "question": "In Docker, what instruction is used to set the default executing command?",
        "options": ["RUN", "ENV", "CMD", "EXPOSE"],
        "answer": "CMD"
    }
]

st.title("💡 Factoid App")
st.subheader("Test your tech knowledge!")
st.write("---")

# Initialize session state for tracking scores and progress
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.quiz_over = False

if not st.session_state.quiz_over:
    q_index = st.session_state.current_question
    current_q = QUIZ_DATA[q_index]

    st.markdown(f"### **Question {q_index + 1} of {len(QUIZ_DATA)}**")
    st.write(current_q["question"])

    # User selection
    user_choice = st.radio("Choose the correct answer:", current_q["options"], key=f"q_{q_index}")

    if st.button("Submit Answer"):
        if user_choice == current_q["answer"]:
            st.success("🎉 Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! The correct answer was: {current_q['answer']}")

        # Move to next question or end
        if q_index + 1 < len(QUIZ_DATA):
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.quiz_over = True
            st.rerun()
else:
    st.balloons()
    st.success("✨ Quiz Completed!")
    st.metric(label="Your Final Score", value=f"{st.session_state.score} / {len(QUIZ_DATA)}")

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_over = False
        st.rerun()
