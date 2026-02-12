import asyncio
import time
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, OneShotBehaviour
from spade.message import Message

# ==========================================
# 1. SENSOR AGENT (The Eyes)
# Behavior: Detects disaster -> Sends INFORM to Coordinator
# ==========================================
class SensorBehaviour(OneShotBehaviour):
    async def run(self):
        print("Sensor: [PERCEPT] Scanning environment...")
        await asyncio.sleep(2)
        print("Sensor: [EVENT] FIRE detected at Sector 7!")
        
        # Create Message for Coordinator
        msg = Message(to="coordinator_ben@xmpp.jp")  # <--- ENTER COORDINATOR JID
        msg.set_metadata("performative", "inform")       # FIPA-ACL: Informing
        msg.body = "FIRE_SECTOR_7"
        
        await self.send(msg)
        print("Sensor: [ACTION] Alert sent to Coordinator.")

class SensorAgent(Agent):
    async def setup(self):
        self.add_behaviour(SensorBehaviour())

# ==========================================
# 2. COORDINATOR AGENT (The Brain)
# Behavior: Receives INFORM -> Decides -> Sends REQUEST to Rescuer
# ==========================================
class CoordinatorBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10) # Wait for message
        if msg:
            performative = msg.get_metadata("performative")
            print(f"Coordinator: Received '{performative}' from {msg.sender}: {msg.body}")
            
            # Logic: If it's a fire, order a rescue
            if "FIRE" in msg.body:
                print("Coordinator: [DECISION] Critical situation! Dispatching Rescue Team.")
                
                # Create Order for Rescuer
                order = Message(to="rescuer_son@xmpp.jp") # <--- ENTER RESCUER JID
                order.set_metadata("performative", "request") # FIPA-ACL: Requesting action
                order.body = "EXTINGUISH_FIRE_SECTOR_7"
                
                await self.send(order)
                print("Coordinator: [ACTION] Dispatch order sent.")

class CoordinatorAgent(Agent):
    async def setup(self):
        self.add_behaviour(CoordinatorBehaviour())

# ==========================================
# 3. RESCUE AGENT (The Muscle)
# Behavior: Receives REQUEST -> Executes Action
# ==========================================
class RescueBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            performative = msg.get_metadata("performative")
            
            if performative == "request":
                print(f"RescueAgent: [ORDER RECEIVED] '{msg.body}' from Command.")
                print("RescueAgent: [ACTION] Deploying squad to Sector 7! Go! Go! Go!")
            else:
                print(f"RescueAgent: Message received: {msg.body}")

class RescueAgent(Agent):
    async def setup(self):
        self.add_behaviour(RescueBehaviour())

# ==========================================
# MAIN EXECUTION
# ==========================================
async def main():
    # --- CONFIGURATION (Enter your 3 accounts here) ---
    SENSOR_JID = "sensor_eli@xmpp.jp"
    SENSOR_PASS = "ZH25N@XEpqr!Ab9"
    
    COORD_JID = "coordinator_ben@xmpp.jp"
    COORD_PASS = "@QSZrdXii5zq4f3"
    
    RESCUE_JID = "rescuer_son@xmpp.jp"
    RESCUE_PASS = "pRsh58KinmJb9X!"
    # -------------------------------------------------

    print("System: Initializing Disaster Response Network...")
    
    # 1. Start Receiver Agents First (so they are ready to listen)
    coordinator = CoordinatorAgent(COORD_JID, COORD_PASS)
    await coordinator.start()
    
    rescuer = RescueAgent(RESCUE_JID, RESCUE_PASS)
    await rescuer.start()
    
    # 2. Start Sensor Agent (Trigger the chain)
    sensor = SensorAgent(SENSOR_JID, SENSOR_PASS)
    await sensor.start()
    
    # 3. Let the simulation run
    await asyncio.sleep(10)
    
    # 4. Cleanup
    await sensor.stop()
    await coordinator.stop()
    await rescuer.stop()
    print("System: Simulation complete.")

if __name__ == "__main__":
    asyncio.run(main())