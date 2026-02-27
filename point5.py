import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("healthcare_iot_target_dataset.csv")

# Simulate first 100 records as real-time stream
subset = df.head(100)

# =====================
# Figure 4.15: Heart Rate Over Time
# =====================
plt.figure(figsize=(10,5))
plt.plot(subset["Heart_Rate (bpm)"], color="blue")
plt.title("Figure 4.15: Simulated Real-Time Heart Rate Monitoring")
plt.xlabel("Sample Index")
plt.ylabel("Heart Rate (bpm)")
plt.savefig("fig_4_15_realtime_hr.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.16: Blood Pressure Over Time
# =====================
plt.figure(figsize=(10,5))
plt.plot(subset["Systolic_BP (mmHg)"], label="Systolic BP", color="red")
plt.plot(subset["Diastolic_BP (mmHg)"], label="Diastolic BP", color="green")
plt.title("Figure 4.16: Simulated Real-Time Blood Pressure Monitoring")
plt.xlabel("Sample Index")
plt.ylabel("Blood Pressure (mmHg)")
plt.legend()
plt.savefig("fig_4_16_realtime_bp.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.17: Temperature Over Time
# =====================
plt.figure(figsize=(10,5))
plt.plot(subset["Temperature (°C)"], color="orange")
plt.title("Figure 4.17: Simulated Real-Time Temperature Monitoring")
plt.xlabel("Sample Index")
plt.ylabel("Temperature (°C)")
plt.savefig("fig_4_17_realtime_temp.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.18: Device Battery Level Over Time
# =====================
plt.figure(figsize=(10,5))
plt.plot(subset["Device_Battery_Level (%)"], color="purple")
plt.title("Figure 4.18: Simulated Device Battery Level Monitoring")
plt.xlabel("Sample Index")
plt.ylabel("Battery Level (%)")
plt.savefig("fig_4_18_realtime_battery.png", dpi=300, bbox_inches="tight")
plt.close()

print("Real-time simulation figures (4.15–4.18) generated successfully!")
