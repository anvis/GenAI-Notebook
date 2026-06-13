import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

# Make sure your API key is not hard-coded; set env var first.
API_KEY = "AQ."

@tool
def check_interest_rate() -> str:
    """Provides current loan interest rate"""
    return "Current auto loan interest rate is 8.5%."

@tool
def check_eligibility(age: int = None, salary: int = None) -> str:
    """Checks eligibility criteria for auto loans"""
    if age is not None:
        if age < 21 or age > 60:
            return "Not eligible: age should be between 21 and 60."
    if salary is not None:
        if salary < 25000:
            return "Not eligible: minimum salary is ₹25,000/month."
    return "Eligibility: Minimum salary ₹25,000/month, age 21–60."

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=API_KEY)
agent = create_agent(llm, [check_interest_rate, check_eligibility])

def extract_ai_reply(agent_result) -> str:
    if agent_result is None:
        return ""

    # builtins for dictlike output
    if isinstance(agent_result, dict):
        if 'messages' in agent_result:
            for m in reversed(agent_result['messages']):
                if hasattr(m, 'content'):
                    return str(m.content)
                if isinstance(m, dict):
                    role = m.get('role')
                    content = m.get('content') or m.get('text')
                    if role == 'assistant' and content:
                        return str(content)
        for key in ('output', 'text', 'content'):
            if key in agent_result and agent_result[key]:
                return extract_ai_reply(agent_result[key])
        if 'tool_calls' in agent_result and agent_result['tool_calls']:
            first_call = agent_result['tool_calls'][0]
            return str(first_call.get('output', first_call.get('result', '')))
        return ""

    if isinstance(agent_result, list):
        for item in reversed(agent_result):
            reply = extract_ai_reply(item)
            if reply:
                return reply
        return ""

    # object wrappers
    if hasattr(agent_result, 'content'):
        return str(agent_result.content)
    if hasattr(agent_result, 'text'):
        return str(agent_result.text)
    if hasattr(agent_result, 'message'):
        return extract_ai_reply(agent_result.message)
    if hasattr(agent_result, 'output'):
        return extract_ai_reply(agent_result.output)

    try:
        return str(agent_result)
    except Exception:
        return ""

def run_query(query: str) -> str:
    try:
        raw_result = agent.invoke({"messages": [{"role": "user", "content": query}]})
        #print("INVOKE RESULT:", raw_result)
        return extract_ai_reply(raw_result)
    except Exception as invoke_exc:
        print("Agent.invoke also failed:", invoke_exc)
        return ""
        

if __name__ == "__main__":
    query = "Can you check eligibility for age 45 and salary 30000?"
    print("Query:", query)   
    reply = run_query(query=query)
    print("Reply:", reply)



