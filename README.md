# AIML-Project-Series-2

# College Admission Chatbot

## Overview

This project implements a College Admission Chatbot using the Bard API to answer user queries related to the admission process. The chatbot engages users in a conversation, providing information on admission procedures, requirements, and deadlines. The project utilizes Streamlit and the Streamlit Chat library for a user-friendly interface.

## Requirements

- Python 3.10
- Bard API Key
- Streamlit
- Streamlit Chat

## Setup

1. Clone the repository.


2. Install dependencies.


3. Set up the Bard API key.

    ```python
    os.environ["_BARD_API_KEY"] = "your_bard_api_key"
    ```

## Usage

1. Run the Streamlit app.

    ```bash
    streamlit run main.py
    ```

2. Access the chatbot through the provided Streamlit interface.

3. Enter your admission-related queries in the text input.

4. Engage in a conversation with the chatbot, asking multiple questions if needed.

5. View the chat history and responses displayed in the chat interface.

## Features

1. **Admission-Related Q&A:**
   - The chatbot uses the Bard API to provide answers to queries related to college admission.

2. **User Interaction:**
   - Users can engage in a conversation with the chatbot, asking multiple questions in a single session.

3. **Contextual Understanding:**
   - The chatbot leverages information from previous interactions to provide more personalized responses.

4. **Error Handling and Feedback:**
   - Robust error handling is implemented to manage cases where the chatbot encounters queries it cannot answer.
   - Users receive helpful feedback when their queries cannot be addressed.
