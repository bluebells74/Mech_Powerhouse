# core/units.py
from .base import Quantity, register_si

# Dimensions: [Mass, Length, Time, Temp]
DIM_LENGTH = (0, 1, 0, 0)
DIM_TIME   = (0, 0, 1, 0)
DIM_MASS   = (1, 0, 0, 0)
DIM_FORCE  = (1, 1, -2, 0)
DIM_PRESS  = (1, -1, -2, 0)
DIM_ENERGY = (1, 2, -2, 0)
DIM_POWER  = (1, 2, -3, 0) # Watts

# Register SI Names
register_si(DIM_FORCE, "Newton")
register_si(DIM_PRESS, "Pascal")
register_si(DIM_ENERGY, "Joule")
register_si(DIM_POWER, "Watt")
register_si((0, 0, 0, 0), "Dimensionless")

# --- Unit Functions ---
def Meter(v): return Quantity(v, "m", DIM_LENGTH, 1.0)
def MM(v):    return Quantity(v, "mm", DIM_LENGTH, 0.001)
def Second(v): return Quantity(v, "s", DIM_TIME, 1.0)
def RPM(v):   return Quantity(v, "rpm", (0, 0, -1, 0), 1/60.0) # Frequency

def Newton(v): return Quantity(v, "N", DIM_FORCE, 1.0)
def Pascal(v): return Quantity(v, "Pa", DIM_PRESS, 1.0)
def MPa(v):    return Quantity(v, "MPa", DIM_PRESS, 1e6)
def GPa(v):    return Quantity(v, "GPa", DIM_PRESS, 1e9)

def Nm(v):     return Quantity(v, "Nm", DIM_ENERGY, 1.0) # Torque/Energy
def kW(v):     return Quantity(v, "kW", DIM_POWER, 1000.0)
def Kg(v):     return Quantity(v, "kg", DIM_MASS, 1.0)