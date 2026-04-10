class MCPChatbot:
    def __init__(self, agent):
        self.agent = agent
        self.message_history = []
    
    async def process_chat(self, user_input):
        try:
            self.message_history.append({"role": "user", "content": user_input})
            response = await self.agent.ainvoke({"messages": self.message_history})
            self.message_history.append({"role": "assistant", "content": response['messages'][-1].content})
            return response['messages'][-1].content
        except Exception as e:
            return f"Error: {e}"
        
    async def chatloop(self):
    
        print("\nMCP Chatbot Started!")
        print("Type your queries or 'quit' to exit.\n")
        
        while True:
            user_input = input("Query: ").strip()
            
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            
            response = await self.process_chat(user_input)
            
            print("Assitant:", response)    