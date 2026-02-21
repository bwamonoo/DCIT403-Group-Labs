import asyncio
from spade.agent import Agent
from spade.behaviour import OneShotBehaviour

class GreetingBehaviour(OneShotBehaviour):
    async def run(self):
        my_id = str(self.agent.jid)
        
        print("-------------------------------------------------")
        print(f"SYSTEM STATUS: ONLINE")
        print(f"IDENTITY VERIFIED: {my_id}")
        print("CONNECTION ESTABLISHED: xmpp.jp Server")
        print("I am awake and awaiting instructions.")
        print("-------------------------------------------------")
        
        await self.agent.stop()

class Lab1Agent(Agent):
    async def setup(self):
        print(f"Agent {self.jid} is booting up...")
        self.add_behaviour(GreetingBehaviour())

async def main():
    agent = Lab1Agent("bwamonoo_student@xmpp.jp", "Q86QY4Xni@AbtBf")
    await agent.start()
    
    # Wait for the agent to finish
    while agent.is_alive():
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    asyncio.run(main())