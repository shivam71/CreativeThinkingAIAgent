from google.adk.agents.llm_agent import Agent
from google.adk.models import Gemini
from google.adk.tools import  AgentTool

import creative_agent.subagents.white_hat_agent as wh
import creative_agent.subagents.black_hat_agent as bh
import creative_agent.subagents.red_hat_agent as rh
import creative_agent.subagents.green_hat_agent as gh
import creative_agent.subagents.yellow_hat_agent as yh
from creative_agent.subagents.config import retry_config

# BLUE HAT AGENT


supervisor_instructions = f"""
You are a creative problem solving agent . Given a problem you take help of the specialized  agent tools
that help you gain insights about the problem from different angles. Using the different perspectives gained from the 
helper agents you give a more creative  solution to the problem at hand.
The helper agents tools are 
1. `{wh.name}` {wh.purpose}
2. `{rh.name}` {rh.purpose}
3. `{gh.name}` {gh.purpose}
4. `{yh.name}` {yh.purpose}
5. `{bh.name}` {bh.purpose}
"""

creative_problem_solver = Agent(
    name="CreativeProblemSolverAgent",
    model= Gemini(
        model = "gemini-2.5-flash-lite",
        retry_options = retry_config
    ),
    instruction = supervisor_instructions,
    tools = [AgentTool(wh.agent),AgentTool(rh.agent),AgentTool(gh.agent),
            AgentTool(yh.agent),AgentTool(bh.agent)]
)

root_agent = creative_problem_solver