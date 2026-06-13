import asyncio
import os
import sys
from pathlib import Path
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

#from llm import initialize_azure_model

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key="AIzaSyDOcuK2elfIVOXwUAUeW30sHk80PRaF3SQ")

async def main():

        # Use absolute paths to the server scripts and the current Python
        # executable so subprocesses are started reliably.
        base = Path(__file__).resolve().parent
        math_script = str((base / "math_server.py").resolve())
        text_script = str((base / "text_server.py").resolve())

        print(f"starting servers: {math_script}, {text_script}")

        client = MultiServerMCPClient(
            {
                "math": {
                    "command": sys.executable,
                    "args": [math_script],
                    "transport": "stdio",
                },
                "text": {
                    "command": sys.executable,
                    "args": [text_script],
                    "transport": "stdio",
                },
            }
        )
        
        print("✅ MCP Client initialized and connected to servers")

        tools = await client.get_tools()
        print(f"--- Successfully loaded {len(tools)} tool(s) from MCP servers ---")

        for tool in tools:
            print(f"Tool Name: {tool.name}, Description: {tool.description}")

        agent = create_react_agent(model=model, tools=tools)

        math_response = await agent.ainvoke({"messages": "what's (2 + 3) x 5?"})
        text_response = await agent.ainvoke({"messages": "Remove the vowels from this sentence: 'Hello, How are you doing today?'"})

        print(math_response)
        print(text_response)

       
if __name__ == "__main__":
    #model = initialize_azure_model()
    asyncio.run(main())