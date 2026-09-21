import random


# Our network links
links = [
    ("R1", "R2"),
    ("R2", "R3"),
    ("R3", "R4"),
    ("R4", "R1")
]


# Number of packets sent on each link
packets = 20


# Check each link
for link in links:

    print("\nLink:", link[0], "->", link[1])

    # Store delay values
    delays = []

    # Count lost packets
    lost_packets = 0

    # Send packets
    for i in range(packets):

        # Generate a random delay between 10 and 50 ms
        delay = random.randint(10, 50)

        # Store the delay
        delays.append(delay)

        # Random packet loss
        if random.random() < 0.10:
            lost_packets = lost_packets + 1

    # Calculate average delay
    average_delay = sum(delays) / len(delays)

    # Calculate packet loss percentage
    packet_loss = (lost_packets / packets) * 100

    # Calculate jitter
    jitter = 0

    for i in range(1, len(delays)):
        jitter = jitter + abs(delays[i] - delays[i - 1])

    jitter = jitter / (len(delays) - 1)

    # Display results
    print("Packets sent:", packets)
    print("Packets lost:", lost_packets)
    print("Packet loss:", round(packet_loss, 2), "%")
    print("Average delay:", round(average_delay, 2), "ms")
    print("Jitter:", round(jitter, 2), "ms")