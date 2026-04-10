from mcp_servers.server_config import config
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

from chatbot.chatbot import MCPChatbot
from prompts.system_prompt import SYSTEM_PROMPT

_ = load_dotenv()

import asyncio

async def main():
    
    #llm = ChatGroq(model="llama-3.3-70b-versatile")
    
    llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
    
    # Create MCP client
    client = MultiServerMCPClient(config)
    
    
    tools = await client.get_tools()
    
    tool_info = [tool.name for tool in tools]
    
    print(f"Available Tools: {tool_info}")
    
    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT
    )
    
    chatbot = MCPChatbot(agent)
    
    await chatbot.chatloop()
    

if __name__ == "__main__":
    asyncio.run(main())