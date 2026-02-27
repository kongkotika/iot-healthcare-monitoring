import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_iot_target_dataset.csv")

# =====================
# Figure 4.19: Battery Distribution Histogram
# =====================
plt.figure(figsize=(8,5))
sns.histplot(df["Device_Battery_Level (%)"], bins=20, color="purple", kde=True)
plt.title("Figure 4.19: Distribution of Device Battery Levels")
plt.xlabel("Battery Level (%)")
plt.ylabel("Frequency")
plt.savefig("fig_4_19_battery_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.20: Battery Level Time Trend
# =====================
plt.figure(figsize=(12,5))
plt.plot(df["Device_Battery_Level (%)"].head(300), color="purple")
plt.title("Figure 4.20: Battery Depletion Trend Over Time (First 300 Records)")
plt.xlabel("Sample Index")
plt.ylabel("Battery Level (%)")
plt.savefig("fig_4_20_battery_trend.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.21: Critical Battery Alerts
# =====================
critical = df[df["Device_Battery_Level (%)"] < 20].index
plt.figure(figsize=(12,5))
plt.plot(df["Device_Battery_Level (%)"].head(300), color="gray")
plt.scatter(critical, df.loc[critical, "Device_Battery_Level (%)"], 
            color="red", label="Critical (<20%)")
plt.title("Figure 4.21: Critical Battery Alerts in Monitoring")
plt.xlabel("Sample Index")
plt.ylabel("Battery Level (%)")
plt.legend()
plt.savefig("fig_4_21_battery_alerts.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ Reliability Figures (4.19–4.21) generated successfully!")
