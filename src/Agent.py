from src.utils import connect_to_groq, get_prompt

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

if __name__ == '__main__':
    client_groq = connect_to_groq()
    agent = AgentClass(client_groq, get_prompt())
    result = agent('What is the GDP of india in 2022?')
    print(result)
    print(agent.history)