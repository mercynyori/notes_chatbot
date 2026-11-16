import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


# Model type and the file with my lecture notes
MODEL = "Qwen/Qwen3-30B-A3B-Instruct-2507"
NOTES_FOLDER = "lectures"

# connect to the neibua factory API key
client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1",
    api_key=os.environ["NEBIUS_API_KEY"],
)

# Read every .txt or .md file in the notes folder
notes = ""
for filename in os.listdir(NOTES_FOLDER):
    if filename.endswith((".txt", ".md")):
        path = os.path.join(NOTES_FOLDER, filename)
        with open(path, encoding="utf-8") as f:
            notes += f"\n\n--- {filename} ---\n" + f.read()

print(f"Loaded {len(notes)} characters of notes.")

# system prompt for the output 
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly tutor. Answer questions using ONLY the notes below. "
            "If the answer isn't in the notes, say so.\n\n"
            f"NOTES:\n{notes}"
        ),
    }
]


# if i wanna quit the chatting
print("Ask about your notes (type 'quit' to exit)")
while True:
    question = input("\nYou: ")
    if question.lower() == "quit":
        break

# add the question to the chat so that evrytime you ask a question it will go up and search for it so the longer the question themore the bots has to collect and append all the questions before 
# the max tokens limits the chats output characters

    messages.append({"role": "user", "content": question})
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=800,
    )
    answer = response.choices[0].message.content
    print("\nBot:", answer)
    messages.append({"role": "assistant", "content": answer})

