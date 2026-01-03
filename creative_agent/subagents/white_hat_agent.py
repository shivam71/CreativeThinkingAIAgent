# WHITE HAT AGENT
from google.adk import Agent
from google.adk.models import Gemini
from google.adk.tools import google_search

from creative_agent.subagents.config import retry_config

white_hat_instructions="""You are a specialized agent which helps to give a fact based , unbiased information about the problem you are asked about.
Use the google_search tool to get the facts and data about the problem. Analyze only based on the facts and data.
DO NOT bring any emotional,critical or creative perspectives.
"""


white_hat_agent = Agent(
    name = "WhiteHatAgent",
    model = Gemini(
        model = "gemini-2.5-flash-lite",
        retry_options= retry_config
    ),
    instruction=white_hat_instructions,
    tools=[google_search],
    output_key="white_hat_agent_findings"
)
