import asyncio
from agents import SensorAgent, CoordinatorAgent, RescueAgent

async def run_simulation():
    c_jid = "coordinator_ben@xmpp.jp"
    r_jid = "rescuer_son@xmpp.jp"
    s_jid = "sensor_eli@xmpp.jp"
    c_pwd = "@QSZrdXii5zq4f3"
    r_pwd = "pRsh58KinmJb9X!"
    s_pwd = "ZH25N@XEpqr!Ab9"

    # Initialize Agents
    coordinator = CoordinatorAgent(c_jid, c_pwd)
    rescuer = RescueAgent(r_jid, r_pwd)
    sensor = SensorAgent(s_jid, s_pwd)

    print("--- Initializing Multi-Agent System ---")
    await coordinator.start()
    await rescuer.start()
    await sensor.start()

    print("System Running. Observe the logs below...")
    
    try:
        # Keep the simulation running for 30 seconds
        await asyncio.sleep(30)
    except KeyboardInterrupt:
        pass
    finally:
        await sensor.stop()
        await coordinator.stop()
        await rescuer.stop()
        print("\n--- System Shutdown Gracefully ---")

if __name__ == "__main__":
    asyncio.run(run_simulation())