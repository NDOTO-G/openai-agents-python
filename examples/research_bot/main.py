import asyncio
import sys
from pathlib import Path

# Add the examples directory to Python path
sys.path.append(str(Path(__file__).parent.parent))
import config  # This will load the API key

from .manager import ResearchManager
from agents import Agent, Runner


async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())
