import asyncio
import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class ReactiveBehaviour(CyclicBehaviour):
    async def run(self):
        # PERCEPTION
        heat_level = random.randint(20, 100)
        print(f"Current Heat: {heat_level}°C")
        
        # REACTION (State Transition)
        if heat_level > 80:
            print(">>> STATE: EMERGENCY! (Heat Critical)")
        else:
            print(">>> STATE: NORMAL (Monitoring)")
            
        await asyncio.sleep(2)

class Lab3Agent(Agent):
    async def setup(self):
        self.add_behaviour(ReactiveBehaviour())

async def main():
    agent = Lab3Agent("bwamonoo_student@xmpp.jp", "Q86QY4Xni@AbtBf")
    await agent.start()
    await asyncio.sleep(10)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())