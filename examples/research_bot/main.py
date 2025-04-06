import asyncio
import sys
from pathlib import Path

# Add the src and examples directories to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))
import config  # This will load the API key

from research_bot.manager import ResearchManager
from agents import Agent, Runner


async def main() -> None:
    query = input("What would you like to research? ")
    await ResearchManager().run(query)


if __name__ == "__main__":
    asyncio.run(main())
