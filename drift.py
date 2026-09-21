# Normal traffic level
baseline_traffic = 20


# Current traffic level
current_traffic = 35


# Drift threshold
threshold = 0.50


# Calculate how much traffic increased
increase = (current_traffic - baseline_traffic) / baseline_traffic


# Display traffic values
print("Baseline traffic:", baseline_traffic)
print("Current traffic:", current_traffic)
print("Traffic increase:", round(increase * 100, 2), "%")


# Check for traffic drift
if increase > threshold:
    print("Traffic Drift Detected!")
else:
    print("No Traffic Drift Detected.")