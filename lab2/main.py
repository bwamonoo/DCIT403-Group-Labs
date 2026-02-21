import asyncio
from agents import SensorAgent

async def run_lab2():
    s_jid = "sensor_eli@xmpp.jp"
    s_pwd = "ZH25N@XEpqr!Ab9"

    print("--- Lab 2: Environmental Perception Initiated ---")
    sensor = SensorAgent(s_jid, s_pwd)

    await sensor.start()

    await asyncio.sleep(15)
    
    await sensor.stop()
    print("--- Lab 2: Perception Session Terminated ---")

if __name__ == "__main__":
    asyncio.run(run_lab2())