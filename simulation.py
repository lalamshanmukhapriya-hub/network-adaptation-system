import random


# -----------------------------
# BEFORE ADAPTATION
# -----------------------------

print("----- BEFORE ADAPTATION -----")

traffic_before = 80

delay_before = random.randint(40, 60)

packet_loss_before = random.randint(5, 15)

print("Traffic:", traffic_before)
print("Delay:", delay_before, "ms")
print("Packet loss:", packet_loss_before, "%")


# -----------------------------
# AFTER ADAPTATION
# -----------------------------

print("\n----- AFTER ADAPTATION -----")

# Traffic is distributed through another route
traffic_after = 50

delay_after = random.randint(15, 30)

packet_loss_after = random.randint(0, 5)

print("Traffic:", traffic_after)
print("Delay:", delay_after, "ms")
print("Packet loss:", packet_loss_after, "%")


# -----------------------------
# COMPARISON
# -----------------------------

print("\n----- COMPARISON -----")

print("Traffic before:", traffic_before)
print("Traffic after:", traffic_after)

print("Delay before:", delay_before, "ms")
print("Delay after:", delay_after, "ms")

print("Packet loss before:", packet_loss_before, "%")
print("Packet loss after:", packet_loss_after, "%")