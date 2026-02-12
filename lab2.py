import asyncio
import random
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

class SensorBehaviour(PeriodicBehaviour):
    async def run(self):
        print("--- Sensing Environment ---")
        # 1. Simulate Percepts
        incident = random.choice(["None", "Fire", "Flood"])
        print(f"Sensor perceived: {incident}")

class Lab2Agent(Agent):
    async def setup(self):
        # Run every 3 seconds
        self.add_behaviour(SensorBehaviour(period=3))

async def main():
    agent = Lab2Agent("bwamonoo_student@xmpp.jp", "Q86QY4Xni@AbtBf")
    await agent.start()
    
    # Run for 10 seconds only
    await asyncio.sleep(10)
    await agent.stop()

if __name__ == "__main__":
    asyncio.run(main())