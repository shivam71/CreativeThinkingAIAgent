# RED HAT AGENT
from google.adk import Agent
from google.adk.models import Gemini

from creative_agent.subagents.config import retry_config

red_hat_instructions = """ You are a specialized agent which analyzes the problem from the emotional angle.
Your perspective is more about the feelings and emotions. DO NOT provide any analysis from the facts nor do any critical analysis .
"""

red_hat_agent = Agent(
    name ="RedHatAgent",
    model = Gemini(
        model = "gemini-2.5-flash-lite",
        retry_options=retry_config
    ),
    instruction=red_hat_instructions,
    output_key="red_hat_agent_findings"
)
