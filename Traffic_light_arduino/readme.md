# Arduino Traffic Light – Hardware and Circuit Guide

This project is a simple **traffic light controller**
The system uses three LEDs (red, yellow, green) and runs through a clear sequence of phases using separate functions.

---

## 1. Hardware Requirements

To build the circuit, you need:

- **1 × Arduino Uno** (or compatible board)
- **1 × Breadboard**
- **3 × LEDs**
  - 1× Red LED  
  - 1× Yellow LED  
  - 1× Green LED
- **3 × 220 Ω resistors** (for current limiting)
- **Jumper wires**
- **USB cable** (for programming and power)

---

## 2. Pin Assignments

| LED     | Arduino Pin | Series Resistor | Notes |
|---------|-------------|------------------|-------|
| Red     | `D2`        | 220 Ω → GND      | Long leg to the pin |
| Yellow  | `D3`        | 220 Ω → GND      | Long leg to the pin |
| Green   | `D4`        | 220 Ω → GND      | Long leg to the pin |

**LED orientation:**
- **Long leg (anode)** → Arduino digital pin  
- **Short leg (cathode)** → Resistor → GND  

## 4. How It Works (Hardware Perspective)

- Each LED is connected to a **digital output pin** on the Arduino.
- The Arduino sends **HIGH** (5V) to turn an LED ON, and **LOW** (0V) to turn it OFF.
- Only **one LED** is turned on at a time in this project, mimicking a real traffic light.