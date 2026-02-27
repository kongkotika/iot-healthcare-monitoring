import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_iot_target_dataset.csv")

# =====================
# Figure 4.8: Heart Rate Trend Over Time
# =====================
plt.figure(figsize=(12,5))
plt.plot(df["Heart_Rate (bpm)"].head(300), color="blue")
plt.title("Figure 4.8: Heart Rate Trend Over Time (First 300 Records)")
plt.xlabel("Sample Index")
plt.ylabel("Heart Rate (bpm)")
plt.savefig("fig_4_8_heart_rate_trend.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.9: Distribution of Health Status
# =====================
plt.figure(figsize=(6,4))
sns.countplot(x="Target_Health_Status", hue="Target_Health_Status",
              data=df, palette="Set2", legend=False)
plt.title("Figure 4.9: Distribution of Health Status Classes")
plt.xlabel("Health Status")
plt.ylabel("Count")
plt.savefig("fig_4_9_health_status_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.10: Correlation Heatmap
# =====================
plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes(include=['float64','int64']).corr(),
            cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Figure 4.10: Correlation Heatmap of Vitals")
plt.savefig("fig_4_10_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.11: Outlier Detection with Boxplots
# =====================
plt.figure(figsize=(8,6))
sns.boxplot(data=df[["Heart_Rate (bpm)", "Systolic_BP (mmHg)", 
                     "Diastolic_BP (mmHg)", "Temperature (°C)"]])
plt.title("Figure 4.11: Outlier Detection in Physiological Parameters")
plt.savefig("fig_4_11_outliers_boxplot.png", dpi=300, bbox_inches="tight")
plt.close()

print(" EDA Figures (4.8–4.11) generated successfully!")
