# app/main.py
import streamlit as st
from utils import load_and_filter_data, plot_ghi_boxplot, create_summary_table

# Title and description
st.title("BSWO Solar Data Discovery Dashboard")
st.write("Interactive dashboard to visualize solar data insights for Benin, Sierra Leone, and Togo.")

# Interactive widgets
country = st.selectbox("Select a Country", ["Benin", "Sierra Leone", "Togo"])
ghi_threshold = st.slider("Set GHI Threshold (W/m²)", min_value=0, max_value=500, value=100, step=10)

# Dynamic data processing from local CSVs
data = load_and_filter_data(country, ghi_threshold)

# Check if data is empty after filtering
if data.empty:
    st.warning(f"No data available for {country} with GHI > {ghi_threshold} W/m². Try lowering the threshold.")
else:
    # Visualizations
    st.subheader(f"GHI Boxplot for {country}")
    fig = plot_ghi_boxplot(data)
    st.pyplot(fig)

    st.subheader(f"Top Regions Summary for {country} (GHI > {ghi_threshold} W/m²)")
    summary_table = create_summary_table(data, ghi_threshold)
    st.table(summary_table)

# Additional interactivity (button to reset threshold)
if st.button("Reset GHI Threshold"):
    st.experimental_rerun()