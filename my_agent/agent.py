from google.adk.agents.llm_agent import Agent
from google.adk.tools import google_search

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent that uses google search to give uptodate news',
    instruction='Look for all th news in the internet and provide a crisp summary based on the topic',
    tools=[google_search]
)
