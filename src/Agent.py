from src.utils import connect_to_groq

class Agent():
    def __init__(self, client, system_message):
        self.client = client
        self.system_message = system_message
        self.history = []
        if self.system_message:
            self.history.append({'role':'system', 'content':self.system_message})
        
    def __call__(self, question):
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
    agent = Agent(client=client_groq, system_message='You are an expert in Transformer architecture, only answer questions related to transformer architecture, anything apart from it you should respond "sorry this is out of my expertise"')
    print('Memory before the first question: ',agent.history)
    print('----')
    result_1 = agent('What are the different ways of adding positional encodings that can be used in tranformer architecture?')
    print(result_1)
    print('Memory after first question: ',agent.history)
    print('----')
    result_2 = agent('What is the recipe of chocolate cake?')
    print(result_2)
    print('Memory after second question: ', agent.history)
