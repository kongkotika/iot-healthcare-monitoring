import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("healthcare_iot_target_dataset.csv")

# =====================
# Figure 4.5: Missing Values Heatmap (using seaborn instead of missingno)
# =====================
plt.figure(figsize=(8,4))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Figure 4.5: Missing Values Heatmap")
plt.savefig("fig_4_5_missing_values.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.6: Correlation Heatmap After Cleaning
# =====================
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['float64','int64']).corr(), 
            cmap="coolwarm", annot=True, fmt=".2f")
plt.title("Figure 4.6: Correlation Heatmap of Numerical Features")
plt.savefig("fig_4_6_correlation_heatmap.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.7: Distribution of Vitals After Scaling
# =====================
plt.figure(figsize=(10,6))
sns.histplot(df["Heart_Rate (bpm)"], bins=30, kde=True, color="blue", label="Heart Rate")
sns.histplot(df["Systolic_BP (mmHg)"], bins=30, kde=True, color="red", label="Systolic BP")
sns.histplot(df["Diastolic_BP (mmHg)"], bins=30, kde=True, color="green", label="Diastolic BP")
sns.histplot(df["Temperature (°C)"], bins=30, kde=True, color="orange", label="Temperature")
plt.legend()
plt.title("Figure 4.7: Distribution of Vitals After Scaling")
plt.savefig("fig_4_7_vitals_distribution.png", dpi=300, bbox_inches="tight")
plt.close()

print(" Preprocessing Figures (4.5–4.7) generated successfully!")
