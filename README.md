# AI Spoken English Teacher

This is a simple Telegram bot that acts as a spoken English teacher and improver using OpenAI's GPT-3.5 language model. The bot replies to messages sent to it by the user and provides corrections for grammar mistakes, typos, and factual errors in the message. It also asks a follow-up question to encourage further conversation.

**Requirements**
To run the bot, you will need to have the following installed:

Python 3.7 or later
openai Python library
python-telegram-bot Python library
dotenv Python library
You will also need to have an OpenAI API key and a Telegram bot token. You can obtain these by following the instructions provided by OpenAI and Telegram, respectively.

**Installation**
1. Clone this repository:
git clone https://github.com/your-username/ai-spoken-english-teacher.git

2. Install the required Python libraries:
pip install -r requirements.txt

3. Create a .env file in the root directory of the project with the following contents:
OPENAI_API_KEY=<your OpenAI API key>
TOKEN=<your Telegram bot token>

4. Start the bot by running:
python main.py

**Usage**
Once the bot is running, you can start a conversation with it by sending a message to the bot on Telegram. The bot will reply with an introductory message and ask you to start the conversation by asking a question. From there, you can continue the conversation by asking more questions and receiving replies from the bot.

