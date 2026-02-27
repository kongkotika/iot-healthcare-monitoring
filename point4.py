import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
import numpy as np

# Load dataset
df = pd.read_csv("healthcare_iot_target_dataset.csv")

# Features and Target
X = df[["Heart_Rate (bpm)", "Systolic_BP (mmHg)", 
        "Diastolic_BP (mmHg)", "Temperature (°C)", "Device_Battery_Level (%)"]]
y = df["Target_Health_Status"]

# Encode target
le = LabelEncoder()
y = le.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "SVM (RBF Kernel)": SVC(kernel='rbf', probability=True, random_state=42)
}

results = {}
plt.figure(figsize=(8,6))

# Train & Evaluate
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    probs = model.predict_proba(X_test)[:,1]

    # Classification report
    print(f"\n{name} Report:\n", classification_report(y_test, y_pred))

    # ROC curve
    fpr, tpr, _ = roc_curve(y_test, probs)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f"{name} (AUC = {roc_auc:.2f})")

plt.plot([0,1],[0,1],'k--')
plt.title("Figure 4.12: ROC Curves for Models")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.savefig("fig_4_12_roc_curves.png", dpi=300, bbox_inches="tight")
plt.close()

# Confusion Matrix for Random Forest
rf = models["Random Forest"]
y_pred_rf = rf.predict(X_test)
cm = confusion_matrix(y_test, y_pred_rf)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Figure 4.13: Confusion Matrix (Random Forest)")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("fig_4_13_confusion_matrix.png", dpi=300, bbox_inches="tight")
plt.close()

# Feature Importance (Random Forest)
importances = rf.feature_importances_
features = X.columns

plt.figure(figsize=(8,5))
sns.barplot(x=importances, y=features, palette="viridis")
plt.title("Figure 4.14: Feature Importance (Random Forest)")
plt.xlabel("Importance Score")
plt.savefig("fig_4_14_feature_importance.png", dpi=300, bbox_inches="tight")
plt.close()

print(" ML Figures (4.12–4.14) generated successfully!")
