import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize OpenAI client with OpenRouter Base URL
llm_client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Memory dictionary mapping user_id -> list of message dictionaries
user_histories = {}
MAX_MEMORY = 10 # Only remember the last 10 messages (to save tokens)

@dp.message(CommandStart())
async def send_welcome(message: types.Message):
    # Reset memory on /start
    user_id = message.from_user.id
    user_histories[user_id] = [{"role": "system", "content": "You are a helpful AI assistant on Telegram."}]
    await message.reply("Hi! I'm an AI bot powered by GPT-4o-Mini! Memory cleared.")

@dp.message()
async def chat_with_llm(message: types.Message):
    user_id = message.from_user.id
    
    # Initialize basic memory for user if it doesn't exist
    if user_id not in user_histories:
        user_histories[user_id] = [{"role": "system", "content": "You are a helpful AI assistant on Telegram."}]
        
    # Append the user's new message to memory
    user_histories[user_id].append({"role": "user", "content": message.text})
    
    # Trim memory if it gets too long string (keep system prompt at index 0 + last N messages)
    if len(user_histories[user_id]) > MAX_MEMORY + 1:
        user_histories[user_id] = [user_histories[user_id][0]] + user_histories[user_id][-MAX_MEMORY:]

    processing_msg = await message.answer("Thinking...")
    
    try:
        response = await llm_client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=user_histories[user_id] # Send full memory!
        )
        answer = response.choices[0].message.content
        
        # Append the bot's response to memory
        user_histories[user_id].append({"role": "assistant", "content": answer})
        
        await processing_msg.edit_text(answer)
    except Exception as e:
        logging.error(f"Error from LLM: {e}")
        # Remove the last user message from memory if API failed
        user_histories[user_id].pop()
        await processing_msg.edit_text("Sorry, an error occurred while generating the response.")

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())

