# design_script.py
from core.units import MM, Meter, kW, Nm
from core.materials import Steel_1018, Titanium
from components.shaft import Shaft
import math

print("=== SHAFT DESIGNER V1.0 ===")

# 1. Inputs
power = kW(20)      # 20 kW Motor
speed = 3000        # RPM
torque_val = (power.si_value * 60) / (2 * math.pi * speed)
load = Nm(torque_val)

print(f"Load: {power} @ {speed} RPM = {load}")

# 2. Design
my_shaft = Shaft(diameter=MM(15), length=Meter(0.2), material=Steel_1018)
print(f"Testing {my_shaft.mat.name} Shaft (D={my_shaft.d})...")

# 3. Analyze
res = my_shaft.analyze_safety(load, required_fos=2.0)
print(f"Result: {res['status']} (FOS: {res['fos']})")

# 4. Swap Material if Failed
if res['status'] == "FAIL":
    print("-> Upgrading to Titanium...")
    my_shaft.mat = Titanium
    res = my_shaft.analyze_safety(load, required_fos=2.0)
    print(f"New Result: {res['status']} (FOS: {res['fos']})")