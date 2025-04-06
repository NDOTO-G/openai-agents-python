import asyncio
import sys
from pathlib import Path

# Add the src and examples directories to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent.parent))
import config  # This will load the API key

from financial_research_agent.manager import FinancialResearchManager


# Entrypoint for the financial bot example.
# Run this as `python -m examples.financial_bot.main` and enter a
# financial research query, for example:
# "Write up an analysis of Apple Inc.'s most recent quarter."
async def main() -> None:
    query = input("Enter a financial research query: ")
    mgr = FinancialResearchManager()
    await mgr.run(query)


if __name__ == "__main__":
    asyncio.run(main())
