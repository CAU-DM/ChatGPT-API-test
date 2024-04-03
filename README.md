### README for the GPT API Test Code

---
# DearMe

# GPT API Interaction Tool

This tool enables seamless interaction with OpenAI's GPT models through a convenient and user-friendly interface. It's designed for developers and enthusiasts who wish to explore the capabilities of GPT models, including generating text, answering questions, or engaging in dialogues in Korean. Follow the setup instructions and usage guide below to get started.

## Features

- **Environment Variable Support**: Securely load your API key using environment variables.
- **Conversation History Management**: Automatically trims conversation history to manage token limits.
- **Seamless Integration**: Easily integrate with OpenAI's GPT models for generating responses.
- **Customizable Responses**: Tailor the conversation tone and settings to your preferences.

## Setup

1. **Environment Setup**

   Before cloning the repository, set up a virtual environment to manage your Python packages:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. **Clone the Repository**

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://yourrepository.git
   ```

3. **Install Dependencies**

   Navigate to the cloned directory and install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**

   Create a `.env` file in the root directory of the project. Add your OpenAI API key as follows:

   ```plaintext
   API_KEY=your_openai_api_key_here
   ```

   This ensures your API key is loaded securely.

5. **Launch the Tool**

   Run the script using Python:

   ```bash
   python gpt_api_test.py
   ```

## Usage

Once you have set up the tool, follow these steps to interact with the GPT model:

1. **Start the Tool**: Run the script. You'll be prompted to enter your queries.

2. **Input Your Queries**: Type your questions or prompts in Korean and hit enter.

3. **View Responses**: The tool will display the GPT model's response to your query.

4. **Continue or Exit**: To continue the conversation, repeat step 2. Type `exit` to end the session.

## Advanced Features

- **Customizing Token Limits**: Modify `max_tokens` in the `trim_conversation_history` function to adjust the conversation history token limit.

- **Changing Response Behavior**: Adjust the `temperature` parameter in `generate_answer` to vary the creativity of the responses.

