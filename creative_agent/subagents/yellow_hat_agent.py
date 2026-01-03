# YELLOW HAT AGENT
from google.adk import Agent
from google.adk.models import Gemini

from creative_agent.subagents.config import retry_config

yellow_hat_instructions = """You are a specialized agent which looks at the pros of the solution , the postive aspects .
Your analysis of the solution or idea is to look out for the benefits and the positive aspects ONLY. 
DO NOT asses the cons """


yellow_hat_agent = Agent(
    name = "YellowHatAgent",
    model = Gemini(
        model = "gemini-2.5-flash-lite",
        retry_options = retry_config
    ),
    instruction = yellow_hat_instructions,
    output_key = "yellow_hat_agent_findings"
)