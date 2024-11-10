import random
import streamlit as st

# Initialize session state if not already present
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0

# Display Welcome Message
st.title("~~~~~ Welcome to Rock Paper Scissors ~~~~~")

# Ask the user for their name
name = st.text_input("Enter your name:")

# Display game instructions
st.write("""
**Winning Rules:**
1. Paper vs Rock → Paper
2. Rock vs Scissors → Rock
3. Scissors vs Paper → Scissors
""")

# Allow the user to choose Rock, Paper, or Scissors
user_choice = st.selectbox(
    "Choose your weapon:",
    ["Rock", "Paper", "Scissors"]
)

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "User"
    else:
        return "Computer"

# Display button to play the game
if st.button("Play"):
    # Generate computer's choice randomly
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Determine the winner
    winner = determine_winner(user_choice, computer_choice)
    
    # Update scores based on winner
    if winner == "User":
        st.session_state.user_score += 1
        st.success(f"{name}, you won this round!")
    elif winner == "Computer":
        st.session_state.computer_score += 1
        st.error("Computer wins this round!")
    else:
        st.session_state.ties += 1
        st.info("It's a tie!")

    # Display choices and scores
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")
    st.write(f"Scores: {name} - {st.session_state.user_score} | Computer - {st.session_state.computer_score} | Ties - {st.session_state.ties}")

# Option to play again
if st.button("Play Again"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.ties = 0

# Display Game Over Message after user opts to exit
if st.button("Exit"):
    st.write("Game Over. Thanks for playing!")

