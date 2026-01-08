# WHITE HAT AGENT
from creative_agent.subagents.utils import get_agent

instruction="""You are a specialized agent which helps to give a fact based , unbiased information about the problem you are asked about.
Use the google_search tool to get the facts and data about the problem. Analyze only based on the facts and data.
DO NOT bring any emotional,critical or creative perspectives.
"""
purpose = "helps you with bare bones facts and data about the problem"
name = "WhiteHatAgent"
output_key = "white_hat_agent_findings"
agent = get_agent(instruction,name,output_key)
