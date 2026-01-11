In Aadhaar Enrolment & Update Analytics Dashboard 📊
1️⃣ Problem Statement 🧩
The UIDAI Aadhaar ecosystem generates massive volumes of enrolment and update data across states and districts of India. However, this data is published in fragmented, multi-file tabular formats, making it difficult to interpret national trends, regional workload distribution, and operational pressure zones.

The objective of this project is to transform raw UIDAI datasets into a structured, indicator-driven analytics system that supports data-driven decision making for infrastructure planning and governance.

2️⃣ Datasets Used 📂
This project uses official UIDAI aggregated datasets:

📄 Enrolment data (new Aadhaar generation across age groups)

🧾 Demographic update data (name, address, DOB, etc.)

🧬 Biometric update data (fingerprint, iris, photo updates)

Each dataset contains records at date–state–district level and multiple CSV files are merged into a single master dataset for analysis.

3️⃣ Methodology 🧠
🧹 Data loading, cleaning, and standardization

🧮 Feature engineering:

Total Enrolment

Total Demographic Updates

Total Biometric Updates

⚙️ System Load = Total Updates

📊 Migration Pressure Index (MPI) = Updates / (Enrolment + 1)

🗂️ Aggregation at district, state, and national levels

📈 Trend analysis, correlation analysis, and anomaly detection

4️⃣ Data Analysis & Visualisation 📈
The project performs:

📈 National Aadhaar activity trend analysis

🔁 Enrolment vs update workload relationship analysis

🗺️ State-wise system load heatmap

🏆 Top states and districts by operational load

🚨 High-risk district identification using Migration Pressure Index

⚠️ Detection of extreme operational stress zones (anomalies)

All plots, tables, and summary datasets are generated using Python, Pandas, Matplotlib, Seaborn, and Streamlit.

5️⃣ Key Insights 🧠
🔁 Many regions are now update-dominated rather than enrolment-driven

⚠️ Workload is heavily concentrated in a few states and districts

🚨 Some districts show extreme operational pressure, indicating infrastructure stress or high population mobility

🗺️ Aadhaar operations have structurally shifted from expansion-focused to maintenance-driven in many regions

6️⃣ Conclusion 🏁
This project converts complex UIDAI Aadhaar datasets into an actionable decision-support analytics and monitoring framework. The indicator-based approach helps identify workload concentration, regional stress zones, and long-term operational patterns, enabling better planning, resource allocation, and governance.

🛠️ Tech Stack
🐍 Python

🧮 Pandas

📊 Matplotlib, Seaborn

🖥️ Streamlit

📁 Project Structure
aadhar/
├── analysis/     # Jupyter notebooks (data processing & indicators)
├── dashboard/    # Streamlit dashboard
├── data/         # Raw UIDAI datasets
├── outputs/      # Generated plots, CSVs, summaries
├── README.md


👩‍💻 Author
Prajusha Dhar
B.Tech IT, Asansol Engineering College
GitHub: https://github.com/Prajusha2004
