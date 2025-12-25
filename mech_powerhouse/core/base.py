# core/base.py

SI_REGISTRY = {}

class Quantity:
    def __init__(self, value, unit_name, dims, conversion_factor=1.0):
        self.value = value
        self.unit_name = unit_name
        self.dims = tuple(dims)
        self.conversion_factor = conversion_factor
        self.si_value = value * conversion_factor

    def __str__(self):
        # Smart printing: Scientific notation for big/small numbers
        if abs(self.value) >= 1000 or (abs(self.value) < 0.01 and self.value != 0):
             return f"{self.value:.2e} {self.unit_name}"
        return f"{self.value:.2f} {self.unit_name}"

    def __repr__(self):
        return f"Quantity({self.value}, '{self.unit_name}', {self.dims})"

    def __add__(self, other):
        if not isinstance(other, Quantity): raise TypeError("Invalid Addition")
        if self.dims != other.dims: raise ValueError(f"Dimension Mismatch: {self.dims} vs {other.dims}")
        new_val = (self.si_value + other.si_value) / self.conversion_factor
        return Quantity(new_val, self.unit_name, self.dims, self.conversion_factor)

    def __sub__(self, other):
        if not isinstance(other, Quantity): raise TypeError("Invalid Subtraction")
        if self.dims != other.dims: raise ValueError(f"Dimension Mismatch")
        new_val = (self.si_value - other.si_value) / self.conversion_factor
        return Quantity(new_val, self.unit_name, self.dims, self.conversion_factor)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Quantity(self.value * other, self.unit_name, self.dims, self.conversion_factor)
        if isinstance(other, Quantity):
            new_si = self.si_value * other.si_value
            new_dims = tuple(a + b for a, b in zip(self.dims, other.dims))
            name = SI_REGISTRY.get(new_dims, "Compound")
            return Quantity(new_si, name, new_dims, 1.0)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Quantity(self.value / other, self.unit_name, self.dims, self.conversion_factor)
        if isinstance(other, Quantity):
            new_si = self.si_value / other.si_value
            new_dims = tuple(a - b for a, b in zip(self.dims, other.dims))
            name = SI_REGISTRY.get(new_dims, "Compound")
            return Quantity(new_si, name, new_dims, 1.0)
            
    def to(self, target_unit, factor):
        return Quantity(self.si_value / factor, target_unit, self.dims, factor)
    
    # --- POWER (Exponentiation) ---
    def __pow__(self, exponent):
        if not isinstance(exponent, (int, float)):
            raise TypeError("Exponent must be a number")
            
        # 1. Power the scalar values
        new_val = self.value ** exponent
        new_si = self.si_value ** exponent
        
        # 2. Multiply the dimension vector by the exponent
        # Example: Length (0,1,0,0) ** 3 becomes Volume (0,3,0,0)
        new_dims = tuple(d * exponent for d in self.dims)
        
        # 3. Resolve the new name (e.g., look for "Volume" in registry)
        base_unit_name = SI_REGISTRY.get(new_dims, f"{self.unit_name}^{exponent}")
        
        return Quantity(new_si, base_unit_name, new_dims, 1.0)

def register_si(dims, name):
    SI_REGISTRY[tuple(dims)] = name