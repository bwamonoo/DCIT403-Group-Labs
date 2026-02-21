import asyncio
import sys
import os
from spade.agent import Agent
from spade.behaviour import PeriodicBehaviour

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sensors.ultrasonic_gauge import UltrasonicDepthGauge

class PerceptionBehaviour(PeriodicBehaviour):
    async def on_start(self):
        # Initialize the hardware interface
        self.instrument = UltrasonicDepthGauge(baseline=3.5)
        print("SensorAgent: [SYSTEM] Ultrasonic Gauge calibrated and online.")

    async def run(self):

        percept = self.instrument.take_reading()

        print(f"SensorAgent: [PERCEPTION] Current reading from gauge: {percept}m")
        
        if percept > 4.5:
            print(f"SensorAgent: [LOGIC] Water level rise observed. Evaluating severity...")

class SensorAgent(Agent):
    async def setup(self):
        self.add_behaviour(PerceptionBehaviour(period=3))