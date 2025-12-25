# core/constants.py
from .base import Quantity

def Const(val, unit, dims): return Quantity(val, unit, dims, 1.0)

g = Const(9.80665, "m/s^2", (0, 1, -2, 0))
pi_approx = 3.14159