# Mech_Powerhouse ⚙️

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

**A professional Python library for mechanical engineering design and analysis.**

Mech_Powerhouse is a computational toolkit designed to bridge the gap between theoretical calculations and software automation. It features a robust **Dimensional Analysis Engine** that ensures unit consistency (SI) across all calculations, preventing common engineering errors in complex designs.

> **Why this project?**
> As mechanical systems become more complex, manual calculations become prone to error. This library provides a type-safe, object-oriented approach to designing machine elements like shafts and bearings, similar to internal tools used at major automotive and industrial firms.

---

## 🚀 Key Features

### 1. Smart Unit System (The Core)
Never worry about unit conversions again. The library handles dimensional analysis automatically.
* **Vector-based Dimensions:** Tracks Mass, Length, Time, and Temperature.
* **Automatic Conversions:** Mix `mm`, `meters`, `MPa`, and `Pascal` seamlessly.
* **Error Prevention:** Prevents illegal operations (e.g., adding *Force* to *Pressure* raises a `ValueError`).

### 2. Shaft Design
Analyze transmission shafts for safety and material compliance.
* **Material Library:** Pre-loaded with standard materials (AISI 1018 Steel, Titanium, etc.).
* **Safety Checks:** Automates Factor of Safety (FOS) calculations against Yield Strength.

---

## 📦 Installation

**Option 1: Direct Install (For Users)**
You can install this library directly into your Python environment from GitHub:

```bash
pip install git+'https://github.com/bluebells74/Mech_Powerhouse.git'
```
**Option 2: Developer Setup (For Contributors)**
If you want to modify the code or run tests:

1. Clone the repository
```bash
git clone 'https://github.com/bluebells74/Mech_Powerhouse.git'
cd Mech_Powerhouse
```
2. Install in editable mode
```bash
pip install -e .
```

## 💻 Usage Examples

**1. Shaft Safety Analysis**

Validate a shaft design against material properties.
```bash
from mech_powerhouse.components.shaft import Shaft
from mech_powerhouse.core.materials import Steel_1018
from mech_powerhouse.core.units import MM, Meter

Create a shaft with specific dimensions and material
drive_shaft = Shaft(diameter=MM(25), length=Meter(0.5), material=Steel_1018)

Check safety factor against a 2000N load
results = drive_shaft.analyze_safety(load=2000, required_fos=2.0)

print(f"Status: {results['status']}")
print(f"Calculated FOS: {results['fos']}")
```
**2. Dimensional Analysis**

The Quantity class ensures your math is physically valid.
```bash
from mech_powerhouse.core.units import Newton, Meter

# Define physical quantities
force = 5000 * Newton
area = 0.0025 * Meter**2  # Area in m²

# Calculate Stress (Automatically detects units as Pascal)
stress = force / area
print(stress)  
# Output: 2.00e+06 Pascal
```
## 🛠️ Project Structure
```bash
MECH_POWERHOUSE/
├── mech_powerhouse/       # Main Library Package
│   ├── core/              # Physics engine (Units, Materials)
│   └── components/        # Engineering elements (Shaft, Bearing)
├── examples/              # Demo scripts showing how to use the code
├── pyproject.toml         # Packaging configuration
└── README.md              # Documentation
```

### 📄 License
Distributed under the MIT License. See `LICENSE` for more information.



#### Built by Amruta Patil.
