import asyncio
import sys
import os
from spade.agent import Agent
from spade.behaviour import FSMBehaviour, State, PeriodicBehaviour

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sensors.ultrasonic_gauge import UltrasonicDepthGauge

# State Definitions
STATE_MONITOR = "MONITORING"
STATE_EVALUATE = "EVALUATING"
STATE_RESPOND = "RESPONDING"

class FloodResponseFSM(FSMBehaviour):
    async def on_start(self):
        print("Agent: [FSM] Internal logic initialized.")

class MonitoringState(State):
    async def run(self):
        print(f"\n[STATE: {STATE_MONITOR}] Sampling environment...")

        reading = self.agent.instrument.take_reading()
        print(f"Agent: [PERCEPT] Gauge report: {reading}m")
        
        # Internal Event Trigger 
        if reading > 4.8:
            print("Agent: [EVENT] Critical water level detected!")
            self.set_next_state(STATE_EVALUATE)
        else:
            await asyncio.sleep(2)
            self.set_next_state(STATE_MONITOR)

class EvaluatingState(State):
    async def run(self):
        print(f"[STATE: {STATE_EVALUATE}] Verifying data and assessing risk...")
        await asyncio.sleep(2)
        self.set_next_state(STATE_RESPOND)

class RespondingState(State):
    async def run(self):
        print(f"[STATE: {STATE_RESPOND}] ACTION: Deploying flood barriers. Goal achieved.")
        await asyncio.sleep(2)
        # Reset for further monitoring
        self.set_next_state(STATE_MONITOR)

class EmergencyResponseAgent(Agent):
    async def setup(self):
        # Initialize the hardware instrument internally
        self.instrument = UltrasonicDepthGauge(baseline=4.0)
        
        fsm = FloodResponseFSM()
        fsm.add_state(name=STATE_MONITOR, state=MonitoringState(), initial=True)
        fsm.add_state(name=STATE_EVALUATE, state=EvaluatingState())
        fsm.add_state(name=STATE_RESPOND, state=RespondingState())
        
        # Internal Transitions 
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_EVALUATE)
        fsm.add_transition(source=STATE_EVALUATE, dest=STATE_RESPOND)
        fsm.add_transition(source=STATE_RESPOND, dest=STATE_MONITOR)
        fsm.add_transition(source=STATE_MONITOR, dest=STATE_MONITOR)
        
        self.add_behaviour(fsm)