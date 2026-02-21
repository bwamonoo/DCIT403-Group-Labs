import asyncio
from agents import EmergencyResponseAgent

async def run_lab3():
    agent = EmergencyResponseAgent("bwamonoo_student@xmpp.jp", "Q86QY4Xni@AbtBf")

    print("--- Lab 3: Single-Agent Goal & FSM Logic ---")
    await agent.start()

    await asyncio.sleep(20)
    
    await agent.stop()
    print("--- Lab 3: Simulation Terminated ---")

if __name__ == "__main__":
    asyncio.run(run_lab3())