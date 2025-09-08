🕵️ Network Sniffer & Traffic Analyzer
📌 Project Overview

This project is a Network Sniffer & Traffic Analyzer developed during my internship.
It captures live network packets, stores them in an SQLite database, detects suspicious activities (like port scans), and provides visualization for better understanding of network traffic.

⚙️ Features
📡 Capture live packets (TCP, UDP, ICMP, etc.)
💾 Store captured packets into SQLite database
🚨 Detect suspicious patterns (alerts for port scanning, unusual traffic)
🧪 Simulate malicious traffic (port scanning tests)
📊 Visualize network statistics with graphs

🛠️ Tech Stack
Python 3
Scapy – packet capturing
SQLite3 – database storage
Matplotlib / Pandas – data visualization

📂 Project Structure
├── alert.py           # Detect suspicious activity
├── database.py        # Initialize and manage SQLite database
├── packets.py         # Packet handling & DB insertion
├── sniffer.py         # Main sniffer script (captures traffic)
├── testportscan.py    # Simulates port scan traffic for testing
├── udp.py             # UDP-specific packet capture
├── visualization.py   # Graphical visualization of captured data
├── packets.db         # Database file (created after running)
├── requirements.txt   # Required Python dependencies
└── README.md          # Project documentation

🚀 How to Run
1️⃣ Clone Repository
git clone https://github.com/your-username/network-sniffer.git
cd network-sniffer

2️⃣ Install Requirements
pip install -r requirements.txt

3️⃣ Initialize Database
python database.py

4️⃣ Start Packet Sniffer
# Linux/Mac
sudo python sniffer.py

# Windows (Run CMD as Administrator)
python sniffer.py

5️⃣ Detect Alerts
python alert.py

6️⃣ Generate Test Traffic (Optional)
python testportscan.py

7️⃣ UDP Traffic Sniffing (Optional)
python udp.py

8️⃣ Visualize Traffic
python visualization.py

📊 Example Output
Alerts (from alert.py):
[ALERT] Possible Port Scan Detected from 192.168.1.10

Visualization (from visualization.py):
Graphs of protocol distribution, packet counts, etc.



✅ Summary

This project demonstrates:
Network packet capture & storage
Intrusion detection basics (alerts)
Network visualization for analysis
It is a foundation for building more advanced Intrusion Detection Systems (IDS) and Security Monitoring Tools.
