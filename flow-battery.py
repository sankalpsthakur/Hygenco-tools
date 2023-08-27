import streamlit as st
import pandas as pd

# Streamlit App title
st.title('1MW Solar Plant with VRFB Model')

# Upload solar generation data
uploaded_file = st.file_uploader("Upload your 8760-hour solar generation data as a CSV file", type=['csv'])
if uploaded_file is not None:
    solar_data = pd.read_csv(uploaded_file)

    # Show a preview of the uploaded data
    st.write('Preview of Uploaded Data')
    st.write(solar_data.head())

    # Define VRFB parameters
    st.subheader('VRFB Parameters')
    vrfb_capacity = st.slider('VRFB Capacity (MWh)', min_value=1, max_value=100, value=10)
    vrfb_efficiency = st.slider('VRFB Efficiency (%)', min_value=80, max_value=100, value=90)

    # Model Energy Flow
    st.subheader('Energy Flow Modeling')

    # Initialize variables
    battery_state = 0
    grid_export = 0

    # Initialize empty lists to store results
    battery_states = []
    grid_exports = []

    # Loop through each hour in the 8760 data
    for solar_output in solar_data['solar_output']:
        # Calculate energy flow
        net_output = solar_output - battery_state
        if net_output > 0:
            grid_export += net_output
            battery_state = 0
        else:
            battery_state = min(battery_state - net_output, vrfb_capacity)
        
        # Store results
        battery_states.append(battery_state)
        grid_exports.append(grid_export)

    # Convert results to DataFrame and show
    results = pd.DataFrame({
        'Battery State (MWh)': battery_states,
        'Grid Export (MWh)': grid_exports
    })
    st.write('Results')
    st.write(results)

    # Option to download the results
    download = st.button('Download Results as CSV')
    if download:
        results.to_csv('solar_plant_with_vrfb_results.csv', index=False)
        st.success('Download Complete')
