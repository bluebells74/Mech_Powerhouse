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

### Option 1: Direct Install (For Users)
You can install this library directly into your Python environment from GitHub:

```bash
# 1. Clone the repository
git clone [https://github.com/bluebells74/Mech_Powerhouse.git](https://github.com/bluebells74/Mech_Powerhouse)

# 2. Navigate to the folder
cd Mech_Powerhouse

# 3. Install as a library
pip install -e .
