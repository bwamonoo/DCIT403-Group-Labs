import random

class UltrasonicDepthGauge:
    """
    Models a physical Ultrasonic Sensor measuring water levels.
    """
    def __init__(self, baseline=3.5, noise_factor=0.02):
        self.depth = baseline
        self.noise_factor = noise_factor

    def take_reading(self):
        """
        Simulates a physical reading with environmental change and sensor noise.
        """
        # Simulate the river level rising/falling slightly
        environmental_change = random.uniform(-0.05, 0.25) 
        self.depth += environmental_change
        
        # Add sensor 'jitter' (noise)
        noise = random.uniform(-self.noise_factor, self.noise_factor)
        percept = self.depth + noise
        
        return round(percept, 3)