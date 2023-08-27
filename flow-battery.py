import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title('1 MW Solar Plant with VRFB Storage')

# Upload 8760 data
uploaded_file = st.file_uploader("Upload your 8760 solar data CSV", type=["csv"])

if uploaded_file is not None:
    solar_data = pd.read_csv(uploaded_file)
    st.write("Uploaded data:", solar_data.head())
    
    # Initialize variables
    battery_capacity = 1000  # kWh
    stored_energy = 0  # Initial stored energy in the battery
    charging_efficiency = 0.9  # 90% efficiency
    discharging_efficiency = 0.9  # 90% efficiency

    # Lists to store data for plotting
    stored_energy_list = []
    grid_supply_list = []

    # Loop through the 8760 data
    for solar_output in solar_data['solar_output']:
        # Charge the battery
        if solar_output > 1000:  # If solar output > demand (1MW)
            excess_energy = solar_output - 1000
            stored_energy += excess_energy * charging_efficiency
            grid_supply = 0

        # Discharge the battery
        elif solar_output < 1000:  # If solar output < demand (1MW)
            deficit = 1000 - solar_output
            stored_energy -= deficit / discharging_efficiency
            grid_supply = 0 if stored_energy > 0 else deficit

        # Cap stored energy to battery capacity
        stored_energy = min(stored_energy, battery_capacity)

        # Append data for plotting
        stored_energy_list.append(stored_energy)
        grid_supply_list.append(grid_supply)

    # Plotting
    plt.figure(figsize=(20, 10))
    plt.plot(stored_energy_list, label='Stored Energy (kWh)')
    plt.plot(grid_supply_list, label='Grid Supply (kWh)')
    plt.xlabel('Hour')
    plt.ylabel('kWh')
    plt.legend()
    plt.title('Energy Storage and Grid Supply Over Time')
    plt.show()
