import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
Telegram_TOEKN = os.getenv("Telegram_TOEKN")

INSTRUCTIONS = """I want you to act as a spoken English teacher and improver. I will speak to you in English and you will reply to me in English to practice my spoken English. I want you to keep your reply neat, limiting the reply to 100 words. I want you to strictly correct my grammar mistakes, typos, and factual errors. I want you to ask me a question in your reply. Now let's start practicing, you could ask me a question first. Remember, I want you to strictly correct my grammar mistakes, typos, and factual errors."""
TEMPERATURE = 0.5
MAX_TOKENS = 80
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6

# limits how many questions we include in the prompt
MAX_CONTEXT_QUESTIONS = 20

previous_questions_and_answers = []

def get_response(instructions, previous_questions_and_answers, new_question):
    """Get a response from ChatCompletion

    Args:
        instructions: The instructions for the chat bot - this determines how it will behave
        previous_questions_and_answers: Chat history
        new_question: The new question to ask the bot

    Returns:
        The response text
    """
    # build the messages
    messages = [
        { "role": "system", "content": instructions },
    ]
    # add the previous questions and answers
    for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
        messages.append({ "role": "user", "content": question })
        messages.append({ "role": "assistant", "content": answer })
    # add the new question
    messages.append({ "role": "user", "content": new_question })

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        top_p=1,
        frequency_penalty=FREQUENCY_PENALTY,
        presence_penalty=PRESENCE_PENALTY,
    )
    return completion.choices[0].message.content

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}'+"The AI teacher is here.")
    #await update.message.reply_text(start())

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_question = update.message.text

    response = get_response(INSTRUCTIONS, previous_questions_and_answers, new_question)

    # add the new question and answer to the list of previous questions and answers
    previous_questions_and_answers.append((new_question, response))

    await update.message.reply_text(response)

app = ApplicationBuilder().token(Telegram_TOEKN).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(MessageHandler(filters.TEXT, echo))

app.run_polling()