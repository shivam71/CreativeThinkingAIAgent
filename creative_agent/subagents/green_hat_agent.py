# GREEN HAT AGENT
from google.adk import Agent
from google.adk.models import Gemini

from creative_agent.subagents.config import retry_config

green_hat_instructions = """ You are a specialized agent which thinking of very creative , out of the box ideas for the problem given to you.
You analysis includes new ideas without worrying about the feasibility . DO NOT think from emotional or critical aspects .
"""

green_hat_agent = Agent(
    name = "GreenHatAgent",
    model = Gemini(
        model  = "gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction=green_hat_instructions,
    output_key="green_hat_agent_findings"
)