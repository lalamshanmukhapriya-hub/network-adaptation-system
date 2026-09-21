import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt


# =========================================
# PAGE SETTINGS
# =========================================

st.set_page_config(
    page_title="Control Knowledge Surgery",
    page_icon="🌐",
    layout="wide"
)


# =========================================
# TITLE
# =========================================

st.title("🌐 Control Knowledge Surgery")
st.subheader("Dependency-Aware Autonomous Network Adaptation")

st.write(
    "This prototype monitors network traffic, detects traffic drift, "
    "analyzes dependencies, selects an alternative route, and verifies "
    "network performance after adaptation."
)


# =========================================
# SIDEBAR
# =========================================

st.sidebar.header("⚙️ Network Settings")

traffic = st.sidebar.slider(
    "Current Traffic on R1-R2 (Mbps)",
    min_value=10,
    max_value=100,
    value=35
)

threshold = st.sidebar.slider(
    "Drift Threshold (%)",
    min_value=10,
    max_value=100,
    value=50
)


# =========================================
# CREATE NETWORK
# =========================================

G = nx.Graph()

G.add_edge("R1", "R2")
G.add_edge("R2", "R3")
G.add_edge("R3", "R4")
G.add_edge("R4", "R1")


position = {
    "R1": (0, 1),
    "R2": (2, 1),
    "R3": (2, 0),
    "R4": (0, 0)
}


# =========================================
# 1. NETWORK TOPOLOGY
# =========================================

st.header("1️⃣ Network Topology")

fig, ax = plt.subplots(figsize=(7, 4))

nx.draw(
    G,
    position,
    with_labels=True,
    node_size=2500,
    node_color="lightblue",
    font_size=12,
    font_weight="bold",
    ax=ax
)

ax.set_title("Simulated Network Topology")

st.pyplot(fig)


st.info(
    "The network contains four simulated routers and four communication links."
)


# =========================================
# 2. TRAFFIC SIMULATION
# =========================================

st.header("2️⃣ Traffic & Network State")


# Traffic on each link
traffic_data = {
    "R1-R2": traffic,
    "R2-R3": 35,
    "R3-R4": 30,
    "R4-R1": 25
}


# Calculate network metrics
delay_before = 10 + (traffic // 6)

packet_loss_before = min(
    10,
    max(0, (traffic - 20) // 6)
)

jitter_before = 5 + (traffic // 15)


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "R1-R2 Traffic",
    str(traffic) + " Mbps"
)

col2.metric(
    "Delay",
    str(delay_before) + " ms"
)

col3.metric(
    "Packet Loss",
    str(packet_loss_before) + " %"
)

col4.metric(
    "Jitter",
    str(jitter_before) + " ms"
)


# Traffic table
st.write("### Link Traffic")

st.table({
    "Link": ["R1-R2", "R2-R3", "R3-R4", "R4-R1"],
    "Traffic (Mbps)": [
        traffic,
        traffic_data["R2-R3"],
        traffic_data["R3-R4"],
        traffic_data["R4-R1"]
    ]
})


# =========================================
# 3. DRIFT DETECTION
# =========================================

st.header("3️⃣ Traffic Drift Detection")

baseline = 20

increase = ((traffic - baseline) / baseline) * 100

st.write("**Baseline Traffic:**", baseline, "Mbps")
st.write("**Current Traffic:**", traffic, "Mbps")
st.write("**Traffic Increase:**", round(increase, 2), "%")


if increase > threshold:

    drift_detected = True

    st.error(
        "⚠️ TRAFFIC DRIFT DETECTED"
    )

    st.write(
        "The traffic on R1-R2 has increased significantly compared "
        "with the baseline."
    )

else:

    drift_detected = False

    st.success(
        "✅ No Traffic Drift Detected"
    )


# =========================================
# 4. DEPENDENCY-AWARE KNOWLEDGE GRAPH
# =========================================

st.header("4️⃣ Dependency-Aware Knowledge Graph")

KG = nx.DiGraph()

KG.add_edge(
    "High Traffic",
    "R1-R2 Link"
)

KG.add_edge(
    "R1-R2 Link",
    "Router R2"
)

KG.add_edge(
    "Router R2",
    "Route R1-R2-R3"
)

KG.add_edge(
    "Route R1-R2-R3",
    "Network Delay"
)

KG.add_edge(
    "Network Delay",
    "Network Performance"
)


kg_position = {
    "High Traffic": (0, 2),
    "R1-R2 Link": (1, 1.5),
    "Router R2": (2, 1),
    "Route R1-R2-R3": (3, 0.5),
    "Network Delay": (4, 0),
    "Network Performance": (5, -0.5)
}


fig2, ax2 = plt.subplots(figsize=(12, 4))

nx.draw(
    KG,
    kg_position,
    with_labels=True,
    node_size=2500,
    node_color="lightgreen",
    font_size=9,
    arrows=True,
    ax=ax2
)

ax2.set_title(
    "Dependency Relationship: Traffic → Link → Router → Route → Performance"
)

st.pyplot(fig2)


st.write(
    "The knowledge graph represents how a traffic problem can propagate "
    "through dependent network components."
)


# =========================================
# 5. IMPACT ANALYSIS
# =========================================

st.header("5️⃣ Impact & Dependency Analysis")

if drift_detected:

    st.warning("Affected Components")

    st.write("🔴 R1-R2 communication link")
    st.write("🔴 Router R2")
    st.write("🔴 Current route R1 → R2 → R3")
    st.write("🔴 Network delay")
    st.write("🔴 Packet loss")

else:

    st.success(
        "No significant dependency impact detected."
    )


# =========================================
# 6. ROUTE ADAPTATION
# =========================================

st.header("6️⃣ Route Adaptation")


current_route = ["R1", "R2", "R3"]


if drift_detected:

    st.warning(
        "⚠️ Current route is experiencing high traffic."
    )

    st.write("### Current Route")

    st.code(
        "R1 → R2 → R3"
    )


    # Create weighted graph
    W = nx.Graph()

    W.add_edge(
        "R1",
        "R2",
        weight=100
    )

    W.add_edge(
        "R2",
        "R3",
        weight=2
    )

    W.add_edge(
        "R1",
        "R4",
        weight=2
    )

    W.add_edge(
        "R4",
        "R3",
        weight=2
    )


    # Find alternative route
    alternative_route = nx.shortest_path(
        W,
        source="R1",
        target="R3",
        weight="weight"
    )


    alternative_text = " → ".join(alternative_route)


    st.success(
        "✅ Alternative Route Selected"
    )

    st.code(
        alternative_text
    )


    st.info(
        "The overloaded R1-R2 link is given a high routing cost, "
        "so the system selects the alternative path R1 → R4 → R3."
    )


else:

    alternative_route = current_route

    st.info(
        "No adaptation is required because traffic is within the normal range."
    )


# =========================================
# 7. SIMULATED EXECUTION
# =========================================

st.header("7️⃣ Network Adaptation Execution")


if drift_detected:

    st.write("### Adaptation Action")

    st.write(
        "The system simulates redirecting traffic from the overloaded "
        "route to the alternative route."
    )


    col1, col2 = st.columns(2)

    with col1:

        st.error("BEFORE")

        st.code(
            "R1 → R2 → R3"
        )


    with col2:

        st.success("AFTER")

        st.code(
            alternative_text
        )


else:

    st.info(
        "No network configuration change was required."
    )


# =========================================
# 8. PERFORMANCE VERIFICATION
# =========================================

st.header("8️⃣ Network Performance Verification")


traffic_before = traffic

delay_before = delay_before

packet_loss_before = packet_loss_before


if drift_detected:

    # Simulated improvement after route change
    traffic_after = max(
        10,
        traffic // 2
    )

    delay_after = max(
        10,
        delay_before - 8
    )

    packet_loss_after = max(
        1,
        packet_loss_before - 4
    )

    jitter_after = max(
        3,
        jitter_before - 3
    )

else:

    traffic_after = traffic

    delay_after = delay_before

    packet_loss_after = packet_loss_before

    jitter_after = jitter_before


col1, col2 = st.columns(2)


# BEFORE
with col1:

    st.subheader("🔴 Before Adaptation")

    st.metric(
        "Traffic",
        str(traffic_before) + " Mbps"
    )

    st.metric(
        "Delay",
        str(delay_before) + " ms"
    )

    st.metric(
        "Packet Loss",
        str(packet_loss_before) + " %"
    )

    st.metric(
        "Jitter",
        str(jitter_before) + " ms"
    )


# AFTER
with col2:

    st.subheader("🟢 After Adaptation")

    st.metric(
        "Traffic",
        str(traffic_after) + " Mbps"
    )

    st.metric(
        "Delay",
        str(delay_after) + " ms"
    )

    st.metric(
        "Packet Loss",
        str(packet_loss_after) + " %"
    )

    st.metric(
        "Jitter",
        str(jitter_after) + " ms"
    )


# =========================================
# 9. ADAPTATION HISTORY
# =========================================

st.header("9️⃣ Adaptation History")


if drift_detected:

    history = [
        "✓ Traffic drift detected on R1-R2",
        "✓ Dependency analysis performed",
        "✓ Router R2 identified as affected",
        "✓ Current route marked as overloaded",
        "✓ Alternative route R1 → R4 → R3 selected",
        "✓ Simulated route adaptation completed",
        "✓ Network performance verified"
    ]

    for item in history:
        st.write(item)

else:

    st.write(
        "No adaptation event has occurred because the network "
        "is currently operating within the configured threshold."
    )


# =========================================
# 10. SYSTEM SUMMARY
# =========================================

st.header("🔟 System Summary")


if drift_detected:

    st.success(
        "Network adaptation was successfully triggered. "
        "Traffic drift was detected, affected dependencies were "
        "identified, an alternative route was selected, and the "
        "result was verified using simulated performance metrics."
    )

else:

    st.info(
        "The network is operating normally. "
        "No adaptation was required."
    )


# =========================================
# PROJECT MAPPING
# =========================================

st.header("📌 Architecture Mapping")

st.table({
    "Architecture Component": [
        "Data Acquisition",
        "Network Perception",
        "Drift Detection",
        "Knowledge Graph",
        "Impact Analysis",
        "Adaptation Planner",
        "Execution",
        "Verification",
        "Dashboard"
    ],

    "Prototype Implementation": [
        "Simulated traffic and network metrics",
        "NetworkX topology",
        "Threshold-based drift detection",
        "NetworkX dependency graph",
        "Dependency traversal",
        "Weighted shortest-path selection",
        "Simulated route change",
        "Before/after metrics",
        "Streamlit dashboard"
    ]
})