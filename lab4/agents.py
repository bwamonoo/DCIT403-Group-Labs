import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour, PeriodicBehaviour
from spade.message import Message
from sensors.ultrasonic_gauge import UltrasonicDepthGauge

# ---------------------------------------------------------
# 1. SENSOR AGENT: Perception & Informing
# ---------------------------------------------------------
class WaterMonitoring(PeriodicBehaviour):
    async def on_start(self):
        self.instrument = UltrasonicDepthGauge()
        self.threshold = 4.6
        self.alert_sent = False

    async def run(self):
        reading = self.instrument.take_reading()
        print(f"SensorAgent: [PERCEPT] Water Level is {reading}m")

        if reading >= self.threshold and not self.alert_sent:
            print(f"SensorAgent: [LOGIC] Critical Threshold Breached!")
            
            # FIPA-ACL INFORM
            msg = Message(to="coordinator_ben@xmpp.jp")
            msg.set_metadata("performative", "inform")
            msg.body = f"FLOOD_DETECTED:{reading}m"
            await self.send(msg)
            self.alert_sent = True

class SensorAgent(Agent):
    async def setup(self):
        self.add_behaviour(WaterMonitoring(period=3))

# ---------------------------------------------------------
# 2. COORDINATOR AGENT: Decision & Delegation
# ---------------------------------------------------------
class DispatchBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            if msg.get_metadata("performative") == "inform":
                print(f"Coordinator: [ACL] Received Status: {msg.body}")
                
                # FIPA-ACL REQUEST
                order = Message(to="rescuer_son@xmpp.jp")
                order.set_metadata("performative", "request")
                order.body = "DEPLOY_FLOOD_BARRIERS_SECTOR_7"
                await self.send(order)
                print("Coordinator: [ACL] Requested action from Rescue Unit.")

class CoordinatorAgent(Agent):
    async def setup(self):
        self.add_behaviour(DispatchBehaviour())

# ---------------------------------------------------------
# 3. RESCUE AGENT: Action Execution
# ---------------------------------------------------------
class ActionBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            if msg.get_metadata("performative") == "request":
                print(f"RescueUnit: [ACL] Order Received: {msg.body}")
                print("RescueUnit: [ACTION] Deploying emergency flood barriers...")

class RescueAgent(Agent):
    async def setup(self):
        self.add_behaviour(ActionBehaviour())