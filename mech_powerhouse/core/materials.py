# core/materials.py
from .units import MPa, GPa, Kg, Meter

class Material:
    def __init__(self, name, density, yield_strength, elastic_modulus):
        self.name = name
        self.density = density
        self.yield_strength = yield_strength
        self.E = elastic_modulus

Steel_1018 = Material("AISI 1018 Steel", Kg(7850)/Meter(1)**3, MPa(370), GPa(205))
Alu_6061   = Material("6061-T6 Aluminum", Kg(2700)/Meter(1)**3, MPa(276), GPa(68.9))
Titanium   = Material("Ti-6Al-4V", Kg(4430)/Meter(1)**3, MPa(880), GPa(113.8))