# AI Telegram Chatbot with Memory 🤖

A highly responsive, asynchronous Telegram chatbot powered by AI models via [OpenRouter](https://openrouter.ai/). Built with Python and `aiogram`, this bot features a smart sliding-window conversation memory to remember past messages contextually within a chat session without exceeding token limits.

## ✨ Features
- **Context-Aware Memory**: Remembers the last 10 messages of the conversation for seamless, intelligent chatting.
- **Model Agnostic / OpenRouter Integrated**: Powered by `gpt-4o-mini` via OpenRouter. You can easily hot-swap to any LLM without changing core code.
- **Asynchronous & Fast**: Built on `aiogram` v3 and `AsyncOpenAI` to handle multiple users simultaneously without lagging or crashing.
- **Smart /start Command**: Reset the user's conversation context and clear the memory instantly by typing `/start`.

## 🛠️ Prerequisites
- Python 3.9+
- A valid Telegram Bot API token (from `@BotFather`)
- An API Key from OpenRouter
- [uv](https://github.com/astral-sh/uv) (Fast Python package manager)

## 🚀 Setup & Installation

1. **Clone the repository** (or navigate to the folder):
   ```bash
   git clone https://github.com/SrijanVerma0/Telegram-Chatbot.git
   cd Telegram-Chatbot
   ```

2. **Set up the virtual environment using `uv`:**
   ```bash
   uv venv
   # Activate on Windows:
   .venv\Scripts\activate
   # Activate on Mac/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   # Install dependencies quickly using uv
   uv pip install -r requirements.txt
   ```

4. **How to get a Telegram Bot Token:**
   - Open Telegram and search for **[@BotFather](https://t.me/botfather)**.
   - Send the `/newbot` command and follow the instructions to set a name and username for your bot.
   - Once completed, BotFather will provide you with a **HTTP API Token** (e.g., `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`). Copy this token.

5. **Environment Variables Config:**
   Create a `.env` file in the main folder and add your keys:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   ```

## 🎮 How to Run

Once everything is set up, just start the bot by running the main file:
```bash
python chat.py
```
Open your bot in the Telegram app, hit `/start`, and enjoy chatting with your memory-enabled AI!