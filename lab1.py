import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class GreetingBehaviour(OneShotBehaviour):
    async def run(self):
        print("Lab 1: Agent connected successfully!")
        await self.agent.stop()

class Lab1Agent(Agent):
    async def setup(self):
        self.add_behaviour(GreetingBehaviour())

async def main():
    # REPLACE WITH YOUR CREDENTIALS
    agent = Lab1Agent("your_username@xmpp.jp", "your_password")
    await agent.start()
    
    # Wait for the agent to finish
    while agent.is_alive():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    asyncio.run(main())