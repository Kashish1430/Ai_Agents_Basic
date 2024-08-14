from src.utils import connect_to_groq

client = connect_to_groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Should one be focuing on Ai Agents or Rag (Retrival Augmented Generation) systems as a future proof skill?",
        }
    ],
    model="llama3-8b-8192",
)

if __name__ == '__main__':
    print(chat_completion.choices[0].message.content)