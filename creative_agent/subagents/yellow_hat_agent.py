# YELLOW HAT AGENT
from creative_agent.subagents.utils import get_agent

instruction = """You are a specialized agent which looks at the pros of the solution , the postive aspects .
Your analysis of the solution or idea is to look out for the benefits and the positive aspects ONLY. 
DO NOT asses the cons """
name = "YellowHatAgent"
output_key = "yellow_hat_agent_findings"
purpose = "gives the more positive and optimistic ideas "
agent = get_agent(instruction,name,output_key)