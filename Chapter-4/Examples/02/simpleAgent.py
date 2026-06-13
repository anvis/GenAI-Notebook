from langchain.agents import  create_agent
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI

#@Tool()
def check_interest_rate(_input: str = None):
    # input is ignored; the tool simply returns the current rate
    return "Current auto loan interest rate is 8.5%."

#@Tool()
def check_eligibility(_input: str = None):
    # input is ignored; eligibility criteria are fixed
    return "Eligibility: Minimum salary ₹25,000/month, age 21–60."

tools = [
    Tool(name="InterestRateTool", func=check_interest_rate, description="Provides current loan interest rate"),
    Tool(name="EligibilityTool", func=check_eligibility, description="Checks eligibility criteria for auto loans")
]

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key="AQ.api")
# create_agent expects the LLM as the first argument and tools second
agent = create_agent(llm, tools)

result = agent.invoke({"messages": [{"role": "user", 
                                              "content": "Tell me the eligibility criteria for auto loans"
                                            }]})
#print(result)



# Example user query
#print(agent.run("Tell me the eligibility criteria for auto loans"))

print("\n--- Extracting AI's Final Reply ---")


def extract_ai_reply(agent_result) -> str:
    # agent_result can be dict, list, AIMessage, or object with attributes.
    if agent_result is None:
        return ""

    if hasattr(agent_result, 'to_dict'):
        try:
            return extract_ai_reply(agent_result.to_dict())
        except Exception:
            pass

    if isinstance(agent_result, dict):
        msgs = agent_result.get('messages') or agent_result.get('choices') or []

        if isinstance(msgs, list) and msgs:
            # handle structured output or list of message dicts
            for m in reversed(msgs):
                if isinstance(m, dict):
                    role = m.get('role')
                    content = m.get('content') or m.get('message') or m.get('text')
                    if role == 'assistant' and content:
                        return content
                elif hasattr(m, 'content'):
                    return str(m.content)

        # fallback to standard keys from agent results
        for key in ('output', 'text', 'content'):
            val = agent_result.get(key)
            if val:
                return extract_ai_reply(val)

        return ""

    if isinstance(agent_result, list):
        for item in reversed(agent_result):
            reply = extract_ai_reply(item)
            if reply:
                return reply
        return ""

    if hasattr(agent_result, 'content'):
        return str(agent_result.content)

    if hasattr(agent_result, 'text'):
        return str(agent_result.text)

    if hasattr(agent_result, 'message'):
        return extract_ai_reply(agent_result.message)

    if hasattr(agent_result, 'output'):
        return extract_ai_reply(agent_result.output)

    return str(agent_result)

print(extract_ai_reply(result))