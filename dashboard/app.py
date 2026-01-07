import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Global style
# -----------------------------
plt.style.use("dark_background")
sns.set_theme(style="darkgrid")

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Aadhaar Analytics Dashboard",
    layout="wide",
    page_icon="📊"
)

st.title("📊 Aadhaar Enrolment & Update Analytics Dashboard")
st.write("Decision-support analytics from UIDAI aggregated datasets")

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("../outputs/final_master_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

master = load_data()

# Derived columns (safety)
if "system_load" not in master.columns:
    master["system_load"] = master["total_demo_updates"] + master["total_bio_updates"]

if "migration_pressure_index" not in master.columns:
    master["migration_pressure_index"] = (
        (master["total_demo_updates"] + master["total_bio_updates"]) /
        (master["total_enrolment"] + 1)
    )

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("🎛 Filters")

states = sorted(master["state"].unique().tolist())
selected_state = st.sidebar.selectbox("Select State", ["All"] + states)

if selected_state != "All":
    df_state = master[master["state"] == selected_state]
    districts = sorted(df_state["district"].unique().tolist())
    selected_district = st.sidebar.selectbox("Select District", ["All"] + districts)
else:
    selected_district = "All"

# Apply filters
filtered = master.copy()

if selected_state != "All":
    filtered = filtered[filtered["state"] == selected_state]

if selected_district != "All":
    filtered = filtered[filtered["district"] == selected_district]

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("📌 Key Indicators")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Enrolment", int(filtered["total_enrolment"].sum()))
c2.metric("Total Demo Updates", int(filtered["total_demo_updates"].sum()))
c3.metric("Total Bio Updates", int(filtered["total_bio_updates"].sum()))
c4.metric("Avg Migration Pressure", round(filtered["migration_pressure_index"].mean(), 2))

# -----------------------------
# 1️⃣ Time Series (COLORED)
# -----------------------------
st.subheader("📈 Activity Over Time")

ts = filtered.groupby("date", as_index=False)[
    ["total_enrolment", "total_demo_updates", "total_bio_updates"]
].sum()

fig1, ax1 = plt.subplots()

ax1.plot(ts["date"], ts["total_enrolment"], label="Enrolment", color="#00E5FF", linewidth=2)
ax1.plot(ts["date"], ts["total_demo_updates"], label="Demographic Updates", color="#FF9100", linewidth=2)
ax1.plot(ts["date"], ts["total_bio_updates"], label="Biometric Updates", color="#00E676", linewidth=2)

ax1.legend()
ax1.set_title("Aadhaar Activity Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Count")

st.pyplot(fig1)

# -----------------------------
# 2️⃣ SCATTER PLOT (COLORED BY RISK)
# -----------------------------
st.subheader("🔵 Enrolment vs System Load (Color = Migration Pressure)")

fig2, ax2 = plt.subplots()

sc = ax2.scatter(
    filtered["total_enrolment"],
    filtered["system_load"],
    c=filtered["migration_pressure_index"],
    cmap="plasma",
    alpha=0.7
)

ax2.set_xlabel("Total Enrolment")
ax2.set_ylabel("System Load (Total Updates)")
ax2.set_title("Enrolment vs System Load")

plt.colorbar(sc, ax=ax2, label="Migration Pressure Index")

st.pyplot(fig2)

# -----------------------------
# 3️⃣ HEATMAP (BETTER COLORS)
# -----------------------------
st.subheader("🔥 State-wise System Load Heatmap")

state_summary = master.groupby("state", as_index=False)["system_load"].sum()
state_summary = state_summary.sort_values("system_load", ascending=False)

heatmap_data = state_summary.set_index("state")[["system_load"]]

fig3, ax3 = plt.subplots(figsize=(6, 10))

sns.heatmap(
    heatmap_data,
    cmap="rocket",
    linewidths=0.3,
    ax=ax3
)

ax3.set_title("State-wise Aadhaar System Load")

st.pyplot(fig3)

# -----------------------------
# 4️⃣ Top Risk Districts Table (GRADIENT COLOR)
# -----------------------------
st.subheader("🚨 Top High-Risk Districts (Migration Pressure)")

top_risk = master.sort_values("migration_pressure_index", ascending=False).head(20)

st.dataframe(
    top_risk[[
        "date", "state", "district",
        "total_enrolment", "total_demo_updates", "total_bio_updates",
        "migration_pressure_index", "system_load"
    ]].style.background_gradient(
        subset=["migration_pressure_index"],
        cmap="YlOrRd"
    ),
    use_container_width=True
)

# -----------------------------
# Raw Data
# -----------------------------
with st.expander("📄 Show Raw Filtered Data"):
    st.dataframe(filtered, use_container_width=True)