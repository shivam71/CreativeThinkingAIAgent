# GREEN HAT AGENT
from creative_agent.subagents.utils import get_agent

instruction = """ You are a specialized agent which thinking of very creative , out of the box ideas for the problem given to you.
You analysis includes new ideas without worrying about the feasibility . DO NOT think from emotional or critical aspects .
"""
purpose = "gives you very out of the box ideas "
output_key = "green_hat_agent_findings"
name = "GreenHatAgent"
agent = get_agent(instruction,name,output_key)