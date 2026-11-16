# Notes Bot

A command-line chatbot that answers questions about my lecture notes.
It reads my `.txt` and `.md` notes and sends them, along with my question, to an AI model on Nebius Token Factory.
Very helpful for lile reading especially for my language classes.


## Setup

1. Install the dependencies:

   ```
   pip install openai python-dotenv
   ```

2. Create a `.env` file in this folder with your Nebius API key:

   ```
   NEBIUS_API_KEY=your-key-here
   ```

3. Create a folder called `lectures` and put your `.txt` or `.md` notes inside it.

## Run

```
python chat1.py
```

Type a question about your notes. Type `quit` to exit and  erase the chat memory.

## How it works

- Reads every note file in `lectures/` and gives the text to the model as context.
- Keeps the conversation in a list and sends it with every question.
- Saves the chat to `history.json`, so it remembers between sessions.

## Notes

- `.env`, `history.json` and `lectures/` are not uploaded to Git.
- Very large notes get expensive, since everything is sent with each question.

## Built with

Python, the OpenAI Python library (pointed at Nebius), and the model `Qwen/Qwen3-30B-A3B-Instruct-2507`.
