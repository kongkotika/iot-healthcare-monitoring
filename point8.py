import matplotlib.pyplot as plt

stages = [
    "Data Preprocessing",
    "Exploratory Data Analysis",
    "Machine Learning Modeling",
    "Real-Time Simulation & Dashboard",
    "Device Reliability Assessment",
    "Privacy & Security Discussion",
    "Final Framework"
]

y_positions = list(range(len(stages), 0, -1))

plt.figure(figsize=(10,7))

for i, stage in enumerate(stages):
    plt.text(0.5, y_positions[i], stage, ha="center", va="center",
             bbox=dict(boxstyle="round,pad=0.4", facecolor="skyblue", alpha=0.7))

for i in range(len(stages)-1):
    plt.arrow(0.5, y_positions[i]-0.3, 0, -0.4, head_width=0.02, head_length=0.2,
              fc="black", ec="black")

plt.axis("off")
plt.title("Figure 4.24: End-to-End IoT Healthcare Monitoring Workflow", fontsize=12)
plt.savefig("fig_4_24_final_workflow.png", dpi=300, bbox_inches="tight")
plt.close()

print(" Final Workflow Diagram (Figure 4.24) generated successfully!")
