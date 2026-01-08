# RED HAT AGENT
from creative_agent.subagents.utils import get_agent
from creative_agent.subagents.white_hat_agent import purpose

instruction = """ You are a specialized agent which analyzes the problem from the emotional angle.
Your perspective is more about the feelings and emotions. DO NOT provide any analysis from the facts nor do any critical analysis .
"""
purpose = "helps you with the emotional angle of the problem "
name = "RedHatAgent"
output_key = "red_hat_agent_findings"
agent = get_agent(instruction,name,output_key)
