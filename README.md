# Smart Door Alert – Capstone Project (Check-In 1)

## Team Members & Roles
| Name | Primary Role | Secondary Role |
|--------|-------------------------------|-------------------------------|
| Castro N. Fokou | Hardware & Sensor Setup | Documentation |
| Rupesh Nepal | UI & API Design | Storage & MQTT Integration |
Rupesh will also help with testing the UI and REST API functions.
---

## Problem Description
People often forget to close doors, causing security, privacy, and energy-loss issues in shared rooms, student housing, and small indoor environments. There is no affordable or simple real-time way to know if a door has been left open unless someone is present. Our goal is to solve this through a small IoT-based monitoring solution that provides awareness and safety.

---

## Solution Description
We plan to build a Smart Door Alert system using an ESP32 and a magnetic reed switch to detect the open/closed status of a door. MQTT will be used for live state updates, while REST will be used to access stored history. A simple UI will display the status to the user. This system is low-cost, easy to use, and helps improve awareness and safety.

---

## API Paradigms
| API | Purpose |
|------|-----------------------------|
| MQTT | Real-time door status updates |
| REST | Retrieve stored door status history |

---

## Planned Hardware
| Component | Purpose |
|------------|---------|
| ESP32 Board | IoT controller |
| Magnetic Reed Switch | Detect open/closed state |
| LED or Buzzer | Local alert output |
| Jumper wires | Connection |

---

## Planned Repository Structure
/Documentation
    - Stores wiring sketch and project diagrams.

/hardware
    - Contains ESP32 code and sensor-related files.

/software
    - Contains UI files, MQTT subscriber code, and REST API logic.

/data
    - Will be used for storing logs or history data.

/tests
    - Will contain any scripts used for testing the system.

README.md
    - Main documentation file for the project.

api_plan.txt
    - Notes for MQTT topics and REST API endpoints.
