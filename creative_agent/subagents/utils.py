from google.adk import Agent
from google.adk.models import Gemini

from creative_agent.subagents.config import retry_config


def get_agent(instruction, name, output_key):
    return Agent(
        name=name,
        model=Gemini(
            model="gemini-2.5-flash-lite",
            retry_options=retry_config
        ),
        instruction=instruction,
        output_key=output_key
    )