import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("packets.db")
cursor = conn.cursor()

cursor.execute("SELECT proto, COUNT(*) FROM packets GROUP BY proto")
data = cursor.fetchall()

protocols = [row[0] for row in data]
counts = [row[1] for row in data]

plt.bar(protocols, counts)
plt.title("Traffic Summary by Protocol")
plt.xlabel("Protocol")
plt.ylabel("Packet Count")
plt.show()
