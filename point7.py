import matplotlib.pyplot as plt

# =====================
# Figure 4.22: IoT Healthcare Data Flow (Simple Diagram)
# =====================
plt.figure(figsize=(8,6))
plt.text(0.1, 0.8, "Wearable Sensors", bbox=dict(facecolor="skyblue", alpha=0.7))
plt.text(0.4, 0.8, "IoT Gateway", bbox=dict(facecolor="skyblue", alpha=0.7))
plt.text(0.7, 0.8, "Cloud Server", bbox=dict(facecolor="skyblue", alpha=0.7))
plt.text(0.4, 0.5, "Healthcare Dashboard", bbox=dict(facecolor="skyblue", alpha=0.7))
plt.text(0.4, 0.2, "Doctors / Patients", bbox=dict(facecolor="skyblue", alpha=0.7))

# arrows
plt.arrow(0.22, 0.8, 0.15, 0, head_width=0.05, length_includes_head=True)
plt.arrow(0.52, 0.8, 0.15, 0, head_width=0.05, length_includes_head=True)
plt.arrow(0.75, 0.77, -0.25, -0.2, head_width=0.05, length_includes_head=True)
plt.arrow(0.48, 0.47, 0, -0.2, head_width=0.05, length_includes_head=True)

plt.axis("off")
plt.title("Figure 4.22: Secure Data Flow in IoT Healthcare Monitoring")
plt.savefig("fig_4_22_data_flow.png", dpi=300, bbox_inches="tight")
plt.close()

# =====================
# Figure 4.23: Threat Model Layers
# =====================
layers = ["Device Layer", "Network Layer", "Application Layer"]
threats = [3, 2, 1]  # example severity levels

plt.figure(figsize=(7,5))
plt.bar(layers, threats, color=["red","orange","blue"])
plt.title("Figure 4.23: Threat Model Layers in IoT Healthcare")
plt.ylabel("Relative Threat Severity")
plt.savefig("fig_4_23_threat_model.png", dpi=300, bbox_inches="tight")
plt.close()

print("✅ Security Figures (4.22–4.23) generated successfully (no networkx used)!")
