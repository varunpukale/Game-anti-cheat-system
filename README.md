# 🚀 Game Anti-Cheat System

A scalable backend system designed to detect and prevent cheating behaviors in real-time multiplayer environments using rule-based detection and API-driven event ingestion.

---

## 📌 Features

- Real-time event ingestion via REST API
- Rule-based cheat detection engine
- Detection of abnormal behaviors (speed hacks, action spikes)
- Modular and extensible architecture
- Simulation environment for testing player behavior

---

## 🏗️ Architecture

```
Client / Simulator
        ↓
   REST API (Flask)
        ↓
 Cheat Detection Engine
        ↓
 Decision (Allow / Block)
```

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask
- **Architecture:** Modular system design
- **Testing:** Custom player simulator
- **Tools:** Git, GitHub

---

## 📂 Project Structure

```
api/
  server.py
detector/
  cheat_detector.py
  rules.py
simulator/
  player_simulator.py
```

---

## ▶️ How to Run

### 1. Setup environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests
```

### 2. Start server

```bash
python -m api.server
```

### 3. Run simulator

```bash
python simulator/player_simulator.py
```

---

## 🧪 Example Output

```
Normal Player: 200 {'status': 'ok'}
Cheater: 403 {'reason': 'Speed hack detected', 'status': 'blocked'}
```

---

## 🚀 Future Improvements

- Add ML-based anomaly detection
- Integrate streaming systems like Kafka
- Add a real-time monitoring dashboard
- Implement player behavior profiling
- Add persistent logging for suspicious activity

---

## 💡 Key Highlights

- Designed a modular backend system for real-time event processing
- Implemented rule-based detection to identify abnormal player behavior
- Built simulation tools to validate detection logic and system reliability
- Focused on extensibility, clean architecture, and backend security concepts
