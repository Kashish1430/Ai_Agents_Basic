from src.utils import connect_to_groq, get_function_name_and_parameters

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
    action = """
    Thought: I need to get the GDP of India in the year 2022.
    Action: get_gdp: India 2022
    PAUSE
    """
    action_tool_set = get_function_name_and_parameters(action)
    func_name = action_tool_set.group(1)
    params = action_tool_set.group(2)
    print(action_tool_set)
    print(func_name)
    print(params)
    #print(chat_completion.choices[0].message.content)