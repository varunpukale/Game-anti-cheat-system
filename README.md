# 🚀 Game Anti-Cheat System

🚀 Designed with a focus on scalability, low-latency processing, and real-time decision systems used in modern distributed gaming infrastructures.

A scalable backend system designed for real-time cheat detection in multiplayer environments, leveraging rule-based anomaly detection, RESTful APIs, and modular architecture for extensibility and low-latency decision making.

---

## 📌 Features

- Real-time event ingestion via REST API
- Rule-based cheat detection engine
- Detection of abnormal behaviors (speed hacks, action spikes)
- Modular and extensible architecture
- Synthetic workload simulation framework for testing player behavior

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

## 🔗 API Endpoints

### POST /event

Send player event data for cheat detection.

#### Request Body

```json
{
  "user_id": "player1",
  "speed": 120,
  "actions_per_sec": 15
}
```

#### Response

```json
{
  "status": "blocked",
  "reason": "Speed hack detected"
}
```

---

## 📊 Performance

- Handles 1,000+ simulated player events per minute
- Achieves low-latency response times for rule-based detection
- Successfully detects cheating scenarios such as speed hacks and action spikes

---

## 🧪 Example Output

```text
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
- Introduce Redis for fast state tracking and rate-based detection

---

## 💡 Key Highlights

- Designed a modular backend system for real-time event processing
- Implemented rule-based detection to identify abnormal player behavior
- Built simulation tools to validate detection logic and system reliability
- Focused on extensibility, clean architecture, and backend security concepts
- Structured the system to support future scaling into distributed gaming backends
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
