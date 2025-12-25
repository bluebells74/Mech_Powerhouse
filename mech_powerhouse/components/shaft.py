# components/shaft.py
import math
from core.units import Pascal
from core.materials import Material

class Shaft:
    def __init__(self, diameter, length, material):
        self.d = diameter
        self.L = length
        self.mat = material

    def analyze_safety(self, torque, required_fos=2.0):
        # Stress = 16*T / (pi * d^3)
        stress_val = (16 * torque.si_value) / (math.pi * self.d.si_value**3)
        actual_stress = Pascal(stress_val)
        
        # Von Mises Shear Strength ~= 0.577 * Yield
        shear_limit = self.mat.yield_strength * 0.577
        
        fos = shear_limit.si_value / actual_stress.si_value
        status = "SAFE" if fos >= required_fos else "FAIL"
        
        return {"status": status, "fos": round(fos, 2), "stress": actual_stress}