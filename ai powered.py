import random
import time

# Define directions
lanes = ['North', 'South', 'East', 'West']

# Initialize traffic (number of vehicles)
traffic = {
    'North': random.randint(5, 15),
    'South': random.randint(5, 15),
    'East': random.randint(5, 15),
    'West': random.randint(5, 15)
}

# Display traffic data
def show_traffic():
    print("\nCurrent Traffic:")
    for lane in lanes:
        print(f"{lane}: {traffic[lane]} vehicles")

# Decide which lane gets green signal
def ai_decision():
    max_lane = max(traffic, key=traffic.get)
    print(f"\n🚦 Green signal for: {max_lane} (vehicles: {traffic[max_lane]})")
    return max_lane

# Update traffic after green signal
def update_traffic(green_lane):
    # Let 5 vehicles pass from green lane
    traffic[green_lane] = max(0, traffic[green_lane] - 5)
    # Add 1-3 vehicles to other lanes
    for lane in lanes:
        if lane != green_lane:
            traffic[lane] += random.randint(0, 2)

# Run simulation for 5 cycles
for i in range(5):
    print(f"\n--- Time Step {i+1} ---")
    show_traffic()
    green = ai_decision()
    update_traffic(green)
    time.sleep(1)
