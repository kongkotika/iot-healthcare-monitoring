import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================
# Load Dataset
# =====================
df = pd.read_csv("/Users/kongkotika/Downloads/Kongkotika Mondal /archive (5)/healthcare_iot_target_dataset.csv")  # adjust path if needed

# =====================
# Figure 4.1: Dataset Snapshot (Optional as image)
# Save first 10 rows as an image-like table
# =====================
fig, ax = plt.subplots(figsize=(8,3))
ax.axis('tight')
ax.axis('off')
table_data = df.head(10)
ax.table(cellText=table_data.values, colLabels=table_data.columns, loc='center', cellLoc='center')
plt.title("Figure 4.1: Dataset Snapshot (First 10 Rows)")
plt.savefig("fig_4_1_dataset_snapshot.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.2: Distribution of Health Status
# =====================
plt.figure(figsize=(6,4))
sns.countplot(x="Target_Health_Status", hue="Target_Health_Status",
              data=df, palette="Set2", legend=False)
plt.title("Figure 4.2: Distribution of Health Status Classes")
plt.xlabel("Health Status")
plt.ylabel("Count")
plt.savefig("fig_4_2_health_status_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.3: Boxplots of Physiological Parameters
# =====================
plt.figure(figsize=(8,6))
sns.boxplot(data=df[["Heart_Rate (bpm)", "Systolic_BP (mmHg)", 
                     "Diastolic_BP (mmHg)", "Temperature (°C)"]])
plt.title("Figure 4.3: Boxplot of Physiological Parameters")
plt.ylabel("Value")
plt.savefig("fig_4_3_vitals_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.4: Battery Level Trend
# =====================
plt.figure(figsize=(10,5))
plt.plot(df["Device_Battery_Level (%)"].head(200), color="red", linewidth=1.5)
plt.title("Figure 4.4: Battery Level Variation Over Time (First 200 Records)")
plt.xlabel("Sample Index")
plt.ylabel("Battery Level (%)")
plt.savefig("fig_4_4_battery_trend.png", dpi=300, bbox_inches="tight")
plt.close()

print(" Figures 4.1 to 4.4 generated successfully!")
