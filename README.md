# Chloe Chatbot

Chloe is a romantic, caring chatbot with a warm personality, chat memory, and a simple web interface.

## Run the terminal version

```bash
cd /home/mortala/Projects/sam-chatbot
python3 sam_chatbot.py
```

## Run the web version

```bash
cd /home/mortala/Projects/sam-chatbot
python3 app.py
```

Then open:

```text
http://localhost:5000
```

## Features

- More affectionate and realistic responses
- Stores simple memory such as user name and last topic
- Uses a local Ollama model by default, with no API key or per-message charge
- Falls back to OpenAI if `OPENAI_API_KEY` is set and Ollama is unavailable
- Falls back to built-in responses if neither model provider is available
- Voice chat with spoken replies, saved notes, local time/date, and timed reminders while the app is open
- Works as a local terminal bot or a browser chat app

## Personal voice assistant

In a supported browser, choose **Start voice** and allow microphone access. Chloe listens for a turn, speaks her reply, then listens again until you stop voice chat. You can also type these commands:

- `What time is it?`
- `Remember that the spare key is in the desk`
- `Read my notes`
- `Remind me to stretch in 10 minutes`
- `List my reminders`

Notes and reminders are stored in `sam_memory.json`. Reminder alerts appear in the chat while the app is open; the browser does not keep the assistant running after the tab closes.

## Local AI model

Chloe uses Ollama's OpenAI-compatible endpoint and defaults to `gemma4:latest`.
Install Ollama and download a model if needed:

```bash
ollama pull gemma4
```

Set `OLLAMA_MODEL` to use another locally installed model. Set `OLLAMA_BASE_URL`
if Ollama is listening somewhere other than `http://127.0.0.1:11434/v1`.

## Install dependencies

```bash
cd /home/mortala/Projects/sam-chatbot
python3 -m pip install -r requirements.txt
```
