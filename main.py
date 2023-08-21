import streamlit as st
import numpy as np

# Set up Streamlit layout
st.title('Alkaline Electrolyser Specification Tool')

# Sidebar inputs
st.sidebar.title('Input Parameters')

# Get user input
power = st.sidebar.number_input('Power (MW)', min_value=0.1, max_value=10.0, value=1.0)
efficiency = st.sidebar.number_input('Electrolyser Efficiency (%)', min_value=10, max_value=100, value=70)
cell_voltage = st.sidebar.number_input('Cell Voltage (V)', min_value=1.0, max_value=3.0, value=2.0)
current_density = st.sidebar.number_input('Current Density (A/cm²)', min_value=0.1, max_value=2.0, value=0.2)
insulation_efficiency = st.sidebar.number_input('Insulation Efficiency (%)', min_value=10, max_value=100, value=80)
coolant_temp_rise = st.sidebar.number_input('Coolant Temperature Rise (°C)', min_value=1, max_value=20, value=10)
cell_diameter = st.sidebar.number_input('Cell Diameter (m)', min_value=0.1, max_value=2.0, value=1.4)

# Constants
efficiency_frac = efficiency / 100
insulation_efficiency_frac = insulation_efficiency / 100

# Calculations
hydrogen_energy_content = 33.3 # kWh/kg
hydrogen_production_rate = (power * efficiency_frac) / hydrogen_energy_content # kg/s
hydrogen_production_rate_Nm3 = hydrogen_production_rate * (1 / 0.09) * 60 * 60 # conversion from kg/s to Nm3/hr

total_current = power / cell_voltage # Mega Amps
total_active_surface_area = (total_current * 1000 * 1000) / (current_density * 10000) # m²

water_consumption_rate = hydrogen_production_rate_Nm3 * 22.4 # L/hr

heat_generated = power * (1 - efficiency_frac) # MW
heat_to_be_removed = heat_generated / insulation_efficiency_frac # MW

coolant_flow_rate = heat_to_be_removed / (0.753 * coolant_temp_rise) * 60 # L/min

cell_area = np.pi * (cell_diameter / 2) ** 2 # m²
number_of_cells = total_active_surface_area / cell_area

output_voltage = cell_voltage * number_of_cells
output_current = power / output_voltage

# Display results
st.title('Electrolyser Specifications')
st.write(f'Hydrogen Production Rate: {hydrogen_production_rate_Nm3:.2f} Nm³/hr \n (Power * Efficiency / Hydrogen Energy Content)')
st.write(f'Total Current: {total_current:.2f} Mega Ampere')
st.write(f'Total Active Surface Area: {total_active_surface_area:.2f} m² \n (Total Current / (Current Density * 10))')
st.write(f'Water Consumption Rate: {water_consumption_rate:.2f} L/hr \n (Hydrogen Production Rate Nm³/hr * 22.4(molar volume L/Nm³))')
st.write(f'Heat to be Removed: {heat_to_be_removed:.2f} MW \n (Power * (1 - Insulation Efficiency))')
st.write(f'Coolant Flow Rate: {coolant_flow_rate:.2f} L/min \n (Heat to be Removed / (Specific Heat Capacity of KOH * Coolant Temperature Rise) * 60)')

# Component Specifications
st.title('Component Specifications')
st.header('Electrodes')
st.write(f'Cell Area: {cell_area:.2f} m2 \n (Pi * D2/4)')
st.write(f'Number of Cells: {number_of_cells:.2f} \n (Total Active Surface Area / Cell Area)')
st.write(f'Diameter: {cell_diameter:.2f} m')
st.header('Power Supply')
st.write(f'Output Voltage: {output_voltage:.0f} V \n (Cell Voltage * Number of Cells)')
