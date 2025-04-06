import asyncio
import sys
from pathlib import Path

# Add the examples directory to Python path
sys.path.append(str(Path(__file__).parent.parent))
import config  # This will load the API key

from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print(result.final_output)
    # Function calls itself,
    # Looping in smaller pieces,
    # Endless by design.


if __name__ == "__main__":
    asyncio.run(main())
