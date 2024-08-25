from src.utils import connect_to_groq, get_prompt, calculate, get_function_name_and_parameters, get_gdp

class AgentClass():
    def __init__(self, client, system_message):
        self.client = client
        self.system_message = system_message
        self.history = []
        if self.system_message:
            self.history.append({'role':'system', 'content':self.system_message})
        
    def __call__(self, question=""):
        if question:
            self.history.append({'role':'user', 'content': question})

        result = self.get_result()

        self.history.append({'role':'assistant', 'content':result})
        return result
    
    def get_result(self):
        output = self.client.chat.completions.create(messages=self.history, model='llama3-8b-8192')
        return output.choices[0].message.content

    def clear_history(self):
        self.history = []
        self.history.append({'role':'system', 'content':self.system_message})

if __name__ == '__main__':
    client_groq = connect_to_groq()
    agent = AgentClass(client_groq, get_prompt())
    max_iter = 0
    question = 'What is the Ratio of GDP of France in 2023 and GDP of Russia in 2023 ?'
    prompt = question
    tools = ['calculate', 'get_gdp']
    tools_map = {
        'calculate':calculate,
        'get_gdp': get_gdp
    }
    print('--------------')
    while max_iter<5:
        max_iter += 1
        result = agent(str(prompt))

        print('Result Print: ',result)

        if "Answer" in result:
            break

        if "PAUSE" in result and "Action" in result:
            print('Inside Getting Function name')
            action_tool_set = get_function_name_and_parameters(result)
            func_name = action_tool_set.group(1)
            if func_name =='get_gdp':
                params = action_tool_set.group(2).split()
            else:
                params = action_tool_set.group(2)

            if func_name in tools:
                func_name = tools_map.get(func_name)
                if isinstance(params, list):
                    print(f'Calling {func_name}({params})')
                    Observation = func_name(params) #eval(f"{func_name}({params})")
                    prompt = Observation['answer_box']['snippet']
                else:
                    prompt = func_name(params) #eval(f"{func_name}('{params}')")
            else:
                prompt = 'Observation: Tool not Found'
            print('Observation as new prompt: ', prompt)
            continue