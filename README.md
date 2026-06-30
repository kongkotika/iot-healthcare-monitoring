# Real-Time Healthcare Monitoring Using IoT-Enabled Wearable Devices

Master's Thesis project — Informatics, Czech University of Life Sciences Prague (CZU)

## Overview

A real-time healthcare monitoring system that simulates IoT wearable sensor data and uses machine learning to classify patient health status as **Healthy** or **Unhealthy**. The project covers the full pipeline: data preprocessing, exploratory data analysis, predictive modeling, a live-streaming dashboard, device battery reliability analysis, and a privacy/security assessment relevant to IoT healthcare systems.

Dataset: [Healthcare IoT Dataset for Patient Monitoring (Kaggle)](https://www.kaggle.com/datasets/ziya07/healthcare-iot-data) — simulated wearable sensor readings, no real patient data.

## Tech Stack

- **Python** — pandas, scikit-learn
- **Machine Learning** — Logistic Regression, Random Forest, SVM
- **Streamlit** — real-time monitoring dashboard
- **Matplotlib / Seaborn** — data visualization

## Features

- **Data preprocessing**: missing value imputation, duplicate removal, scaling, encoding
- **EDA**: trend analysis, correlation heatmaps, outlier detection across heart rate, blood pressure, and temperature
- **ML classification**: three models compared (Random Forest achieved the best performance — 92% accuracy, 0.91 precision)
- **Real-time simulation dashboard**: live-streamed vitals with color-coded health status and threshold-based alerts
- **Device reliability analysis**: battery depletion trends and estimated continuous uptime (~13 hours)
- **Privacy & security discussion**: encryption, authentication, and compliance considerations (HIPAA/GDPR) for IoT health data

## Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 0.86 | 0.84 | 0.83 | 0.83 |
| **Random Forest** | **0.92** | **0.91** | **0.90** | **0.90** |
| SVM (RBF Kernel) | 0.89 | 0.88 | 0.87 | 0.87 |

Systolic and diastolic blood pressure were the most influential features in predicting patient health status, followed by heart rate.

## How to Run

```bash
pip install pandas scikit-learn streamlit matplotlib seaborn
```

Then run the notebook/scripts in this repo in order: data preprocessing → EDA → model training → Streamlit dashboard. *(See individual files for exact entry points — update this section once you confirm your file names.)*

## Author

Kongkotika Mondal — MSc Informatics, CZU Prague
Supervisor: doc. Ing. RNDr. Petr Zemánek, CSc.
