import streamlit as st
import re
import random
from fuzzywuzzy import fuzz

# Define rule-based responses
rules = [
    (r'(hi|hello|hey)', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m fine, how about you?']),
    (r'i\'m (.*)', ['Hi %1, nice to meet you.'])
]

# Define GPT-based responses
gpt_responses = {
    "What's your favorite color?": "I'm just a computer program, I don't have a favorite color.",
    "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
    "what is your name?": "My name is Chatboat!",
    "What's the capital of France?": "The capital of France is Paris.",
    "Who wrote 'Romeo and Juliet'?": "William Shakespeare wrote 'Romeo and Juliet'.",
    "What's the tallest mountain in the world?": "Mount Everest is the tallest mountain in the world.",
    "Who are you": "i am AI chatboat created by MR.Rafiu Ali Memon",
    "Who discovered gravity?": "Isaac Newton is credited with discovering gravity.",
    "What is the comparative form of 'good'?": "The comparative form of 'good' is 'better.'",
    "Give an example of a preposition.": "An example of a preposition is 'under.'",
    "What is a synonym?": "A synonym is a word that has the same or similar meaning as another word.",
    "What is an algorithm?": "An algorithm is a step-by-step procedure for solving a problem or accomplishing a task.",
    "Define 'RAM'.": "RAM (Random Access Memory) is a type of computer memory that is used to store data and programs that are currently being used by the computer.",
    "What is a browser?": "A browser is a software application used to access information on the World Wide Web.",
    "Explain what a 'byte' is.": "A byte is a unit of digital information that consists of eight bits.",
    "What does 'HTML' stand for?": "HTML stands for Hypertext Markup Language, which is the standard markup language for creating web pages.",
    "Who painted the Mona Lisa?": "Leonardo da Vinci painted the Mona Lisa.",
    "What is the capital of France?": "The capital of France is Paris.",
    "Who wrote the play 'Romeo and Juliet'?": "William Shakespeare wrote 'Romeo and Juliet.'",
    "Which planet is known as the 'Red Planet'?": "Mars is known as the 'Red Planet.'",
    "What is the currency of Japan?": "The currency of Japan is the yen.",
    "What is the holy book of Islam?": "The holy book of Islam is the Quran.",
    "Name the five pillars of Islam.": "The five pillars of Islam are Shahada (faith), Salat (prayer), Zakat (charity), Sawm (fasting), and Hajj (pilgrimage).",
    "Who was the first caliph of Islam?": "Abu Bakr was the first caliph of Islam.",
    "What is the Islamic month of fasting called?": "The Islamic month of fasting is called Ramadan.",
    "Where is the Kaaba located?": "The Kaaba is located in Mecca, Saudi Arabia.",
    "What is the chemical symbol for water?": "The chemical symbol for water is H2O.",
    "What is the unit of measurement for force?": "The unit of measurement for force is the Newton (N).",
    "What is the largest organ in the human body?": "The largest organ in the human body is the skin.",
    "What is the chemical symbol for gold?": "The chemical symbol for gold is Au.",
    "What is the powerhouse of the cell?": "The powerhouse of the cell is the mitochondrion.",
}

# Function to respond to user input using rule-based responses
def respond(input_text):
    for pattern, responses in rules:
        match = re.match(pattern, input_text.lower())
        if match:
            response = random.choice(responses)
            return response

# Function to respond to user input using GPT-based responses with fuzzy matching
def respond_gpt(input_text):
    max_similarity = 0
    best_match = None
    for question in gpt_responses:
        similarity = fuzz.partial_ratio(question.lower(), input_text.lower())
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = question

    # Threshold for similarity score (adjust as needed)
    threshold = 40

    if max_similarity >= threshold:
        return gpt_responses[best_match]
    else:
        return "I'm sorry, I don't understand that."

# Main function to run the chatbot
def main():
    st.title("Rafiu Chatbot")
    st.write("**Welcome to the Chatbot! Start chatting below.**")
    st.write("*Ask basic things about English, Computer, Islamayt, Science, GK, PS*")

    conversation = st.session_state.get("conversation", [])  # Retrieve conversation history

    if "user_input" not in st.session_state:
        st.session_state.user_input = ""

    # Separate variable to track message sent state
    message_sent = False

    user_input = st.text_input("You:", value=st.session_state.user_input)

    if user_input.strip().lower() != "":
        message_sent = True  # Set flag to indicate message sent
        # Save user input
        conversation.append(("You:", user_input))

        response = respond(user_input)  # Check rule-based responses first
        if response:
            st.write("Chatbot:", response)
            # Save chatbot response
            conversation.append(("Chatbot:", response))
        else:
            gpt_response = respond_gpt(user_input)  # If no rule-based response, use GPT-based response
            st.write("Chatbot:", gpt_response)
            # Save chatbot response
            conversation.append(("Chatbot:", gpt_response))

    # Clear the input box only on initial load or after sending a message
    if not message_sent or user_input.strip() == "":
        st.session_state.user_input = ""

    # Update conversation history in session state
    st.session_state.conversation = conversation

    # Display conversation history
    st.write("**Conversation History:**")
    for entry in conversation:
        st.write(f"{entry[0]} {entry[1]}")

# Run the main function to start the Streamlit app
if __name__ == "__main__":
    main()
