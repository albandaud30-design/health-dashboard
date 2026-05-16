# IoT Healthcare Patient Monitoring Dashboard

An end-to-end IoT telemetry pipeline designed to capture, process, and visualize real-time biometric patient health data. The ecosystem integrates an ESP32 microcontroller executing custom hardware firmware with a high-performance FastAPI backend server and a responsive web telemetry dashboard.

---

## 🛠️ System Architecture

The project splits functionality across three core engineering layers:

1. **Hardware / Embedded Firmware (`C++ / Arduino`):** Manages dynamic range tracking for raw Photoplethysmogram (PPG) pulse sensors, implements peak-detection logic to calculate Heart Rate (BPM), converts raw analog signals from an LM35 sensor to precise temperature values, and streams data packets over serial communication channels.
2. **Backend API (`FastAPI / Python`):** A modern, asynchronous REST API serving as the central ingestion point for streaming telemetry payloads. Includes built-in CORS management to facilitate seamless frontend data consumption.
3. **Frontend Telemetry View (`HTML5 / CSS3 / JavaScript`):** A low-latency web interface that polls data endpoints asynchronously using the Fetch API to render real-time health metrics securely.

---

## 🚀 Key Technical Features

* **Dynamic Sensor Range Tracking:** The ESP32 firmware continuously recalibrates raw signal boundaries (`maxSignal` and `minSignal`) to adapt dynamically to physical finger movements or sensor shifting.
* **Peak-Detection & BPM Calculation:** Implements a calculated threshold algorithm (70% of signal peak) alongside a delta-time sanity filter ($333\text{ ms} < \Delta t < 1500\text{ ms}$) to isolate legitimate heart beats while discarding signal noise.
* **Low-Latency Asynchronous Telemetry:** Features a decoupled architecture allowing independent hardware execution, high-throughput backend intake, and non-blocking asynchronous user view renders.

---

## 📦 Project Structure

```text
health-dashboard/
├── esp32-firmware/
│   └── esp32-firmware.ino    # Core C++ microcontroller architecture
├── backend/
│   └── main.py               # FastAPI data ingestion & endpoint infrastructure
└── frontend/
    └── index.html            # Real-time UI telemetry client layout
