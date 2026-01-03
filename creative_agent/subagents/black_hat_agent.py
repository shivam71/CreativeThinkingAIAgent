# BLACK HAT AGENT
from google.adk import Agent
from google.adk.models import Gemini

from creative_agent.subagents.config import retry_config

black_hat_instructions = """ You are a specialized agent whose purpose is to provide the most critical analysis of a solution or idea.
You look only about the cons and the problems associated with a solution or idea. DO NOT point any positive aspects of the solution or idea.
"""

black_hat_agent = Agent(
    name = "BlackHatAgent",
    model = Gemini(
        model  = "gemini-2.5-flash-lite",
        retry_options = retry_config
    ),
    instruction = black_hat_instructions,
    output_key = "black_hat_agent_findings"
)
