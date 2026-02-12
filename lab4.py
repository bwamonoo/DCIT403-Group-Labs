import asyncio
import time
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

# --- 1. SENSOR AGENT (The Eyes) ---
class SensorBehaviour(CyclicBehaviour):
    async def run(self):
        print("Sensor: Scanning area...")
        await asyncio.sleep(5) # Scan every 5 seconds
        
        # Simulate finding a fire
        print("Sensor: [ALERT] Fire detected! Informing Coordinator...")
        
        msg = Message(to="coordinator_student@xmpp.jp") # <--- INSERT COORDINATOR JID
        msg.set_metadata("performative", "inform")
        msg.body = "FIRE_AT_ZONE_1"
        
        await self.send(msg)

class SensorAgent(Agent):
    async def setup(self):
        self.add_behaviour(SensorBehaviour())

# --- 2. COORDINATOR AGENT (The Brain) ---
class CoordinatorBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            print(f"Coordinator: Received info from {msg.sender}: '{msg.body}'")
            
            if "FIRE" in msg.body:
                print("Coordinator: Critical event! Dispatching Rescuer...")
                
                # Send Order to Rescuer
                order = Message(to="rescuer_student@xmpp.jp") # <--- INSERT RESCUER JID
                order.set_metadata("performative", "request") # 'request' means 'do this'
                order.body = "GO_TO_ZONE_1"
                
                await self.send(order)
            else:
                print("Coordinator: Logging minor event.")

class CoordinatorAgent(Agent):
    async def setup(self):
        self.add_behaviour(CoordinatorBehaviour())

# --- 3. RESCUER AGENT (The Muscle) ---
class RescuerBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            if msg.get_metadata("performative") == "request":
                print(f"Rescuer: SIR, YES SIR! Order received: '{msg.body}'. Moving out!")
            else:
                print(f"Rescuer: Received update: {msg.body}")

class RescuerAgent(Agent):
    async def setup(self):
        self.add_behaviour(RescuerBehaviour())

# --- MAIN EXECUTION ---
async def main():
    # SETUP AGENTS
    coordinator = CoordinatorAgent("coordinator_student@xmpp.jp", "pass")
    rescuer = RescuerAgent("rescuer_student@xmpp.jp", "pass")
    sensor = SensorAgent("sensor_student@xmpp.jp", "pass")
    
    # START THEM
    print("System: Booting up agents...")
    await coordinator.start()
    await rescuer.start()
    await sensor.start()
    
    # LET THEM TALK FOR 15 SECONDS
    await asyncio.sleep(15)
    
    # SHUT DOWN
    await sensor.stop()
    await rescuer.stop()
    await coordinator.stop()
    print("System: Shutdown complete.")

if __name__ == "__main__":
    asyncio.run(main())