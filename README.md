# Smart Door Alert – IoT Capstone Project (Check-In 2 Updated)

## 1. Problem Description
In student housing and small shared environments, doors are often left open unintentionally.  
This leads to:

- Security risks  
- Loss of privacy  
- Heat and energy loss  
- No awareness when someone enters or leaves  

There is currently no simple, low-cost system that provides real-time door status notifications.

Our prototype solves this using a **sensor + microcontroller + MQTT messaging** system.

---

## 2. Solution Overview
We built a **Smart Door Alert System** using:

- **ESP8266 NodeMCU** – main controller  
- **Magnetic Reed Switch** – detects OPEN/CLOSED  
- **MQTT (Publish/Subscribe)** – real-time communication  
- **Python UI Subscriber** – displays door events instantly  

This creates a complete end-to-end path:

**Door Sensor → ESP8266 → MQTT Broker → Python UI**

This fully satisfies the *walking skeleton* requirement for Check-In 2.

---

## 3. Hardware Components

| Component | Purpose |
|----------|---------|
| **ESP8266 NodeMCU** | Connects WiFi, reads sensor, publishes MQTT messages |
| **Magnetic Reed Switch** | Detects OPEN (HIGH) / CLOSED (LOW) |
| **LED** | Local visual indicator |
| **Jumper wires / breadboard** | Prototype wiring |

---

## 4. Wiring Diagram (Explanation Only)

### Pins Used
- **D2** → Reed switch signal  
- **3V3** → Reed switch VCC  
- **G** → Ground  
- **D5** → LED output  

### Logic
- Reed = **LOW** → Door CLOSED  
- Reed = **HIGH** → Door OPEN  

A labelled wiring sketch is stored in:
/Documentation/wiring_diagram.png


---

## 5. Architecture Diagram

A clear high-level architecture diagram is stored in:
/Documentation/architecture.png

### Data Flow Description
1. Reed switch changes state  
2. ESP8266 reads input  
3. Publishes `"open"` or `"closed"` to MQTT topic:

   **smartdoor/castro_rupesh/status**

4. Mosquitto broker receives message  
5. Python subscriber prints real-time updates  

This accurately represents the walking prototype.

---

## 6. Software Components

### **1. ESP8266 Firmware**
Located at:
/software/ESP8266 code


Functions:
- Connects to WiFi  
- Connects to MQTT  
- Reads door sensor  
- Controls LED  
- Publishes **open / closed** messages  

---

### **2. Arduino Test Code**
Located at:
/software/Arduino test code

Purpose:
- Validate sensor and LED before adding MQTT logic.

---

### **3. Python MQTT Subscriber (UI)**
Located at:
/software/Subscriber.py

Displays real-time door status updates received from MQTT.

---

## 7. MQTT Topics & API Notes

### **MQTT Topic Used**
smartdoor/castro_rupesh/status
"open"
"closed"


This is documented clearly for future expansion such as storing logs or building a web interface.

---

## 8. Setup Instructions 

These steps allow *any student* to run the project end-to-end.

### **A. Prerequisites**
#### Software
- Arduino IDE (with ESP8266 board installed)  
- Python 3.8+  

Install MQTT library:

```bash
pip install paho-mqtt
```

### **B. Flash the ESP8266 Firmware**
### i. Open Arduino IDE
### ii. Go to:
    /software/ESP8266 code
### iii. Select board: NodeMCU 1.0 (ESP8266)
### iv. Select correct COM port
### v. Upload firmware
### vi. Open Serial Monitor → you should see:
- "WiFi connected"
- "MQTT connected"
- "Door OPEN" / "Door CLOSED"


### **C. Run the Python UI**

Open terminal and run:

cd software

python subscriber.py

Expected output:

Connected to MQTT Broker

Door Status Update → open

Door Status Update → closed


### **D. Test the System**
Move magnet toward/away from reed switch.

### You should see:
- LED turns ON/OFF
- ESP8266 Serial Monitor updates
- Python subscriber prints updates
- All events appear instantly (real-time)


## 9. Repository Structure

/Documentation
    wiring_diagram.png
    architecture.png

/hardware
    test photos and notes

/software
    door_node_test/
    ESP8266 code/
    subscriber.py
    ui_plan.txt

/data
    (future: door history logs)

/tests
    MQTT connection tests, hardware validation tests

README.md
api_plan.txt




