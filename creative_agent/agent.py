from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini
from google.adk.tools import  AgentTool

from creative_agent.subagents.white_hat_agent import white_hat_agent
from creative_agent.subagents.black_hat_agent import black_hat_agent
from creative_agent.subagents.green_hat_agent import green_hat_agent
from creative_agent.subagents.yellow_hat_agent import yellow_hat_agent
from creative_agent.subagents.red_hat_agent import red_hat_agent
from creative_agent.subagents.config import retry_config

# BLUE HAT AGENT

supervisor_instructions = """
You are a creative problem solving agent . Given a problem you take help of the specialized  agent tools
that help you gain insights about the problem from different angles. Using the different perspectives gained from the 
helper agents you give a more creative  solution to the problem at hand.
The helper agents tools are 
1. `WhiteHatAgent` helps you with bare bones facts and data about the problem 
2. `RedHatAgent` helps you with the emotional angle of the problem 
3. `GreenHatAgent` gives you very out of the box ideas 
4. `YellowHatAgent` gives the more positive and optimistic ideas 
5. `BlackHatAgent` is more critical and points out the flaws in the ideas
"""

creative_problem_solver = Agent(
    name="CreativeProblemSolverAgent",
    model= Gemini(
        model = "gemini-2.5-flash-lite",
        retry_options = retry_config
    ),
    instruction = supervisor_instructions,
    tools = [AgentTool(white_hat_agent),AgentTool(red_hat_agent),AgentTool(green_hat_agent),
            AgentTool(yellow_hat_agent),AgentTool(black_hat_agent)]
)

root_agent = creative_problem_solver