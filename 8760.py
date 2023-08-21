
import streamlit as st
import numpy as np

# Title and description
st.title('Electrolyser Vendor Evaluation: 8760')
st.write('For any given GH2 requirement frozen, vendors are asked to quote.')
st.write('1. Rated Power')
st.write('2. $/kW Cost of Electrolyser. ')
st.write('We then calculate the rectifier input power, electrolyser input power, and hydrogen produced based on 8760 solar and wind data to evaluate 3 quotes.')

# User input for 8760 solar and wind data
st.subheader('Enter 8760 Solar and Wind Data')
solar_data = st.text_area('Solar Data (newline-separated values for 8760 hours):')
wind_data = st.text_area('Wind Data (newline-separated values for 8760 hours):')

# User input for transmission losses, rectifier efficiency
transmission_losses = st.number_input('Enter Transmission Losses (in percentage):', min_value=0.0, max_value=100.0, value=4.0)
rectifier_efficiency = st.number_input('Enter Rectifier Efficiency (in percentage):', min_value=0.0, max_value=100.0, value=96.0)

# Rated powers and $/KW for three vendors
vendors = ['Vendor 1', 'Vendor 2', 'Vendor 3']
rated_powers = [st.number_input(f'Enter Rated Power for {vendor}:', min_value=0.0) for vendor in vendors]
dollar_per_kw = [st.number_input(f'Enter $/KW for {vendor}:', min_value=0.0) for vendor in vendors]

# Input for power cost and hydrogen rate
power_cost = st.number_input('Enter Input Power Cost:', value=4.5)
hydrogen_rate = st.number_input('Enter Hydrogen Rate:', value=40)

# Button to perform calculations
if st.button('Calculate & Visualise'):
    try:
        # Parsing the input data
        solar_data = np.array([float(val) for val in solar_data.split('\n')])
        wind_data = np.array([float(val) for val in wind_data.split('\n')])

        # Checking for 8760 data points
        if len(solar_data) != 8760 or len(wind_data) != 8760:
            st.error('Please enter exactly 8760 data points for both solar and wind.')
        else:
            # Calculations for total power and rectifier input power
            total_power = solar_data + wind_data
            rectifier_input_power = (1 - transmission_losses / 100) * total_power

            # Collecting totals for each vendor
            total_electrolyser_input_power = []
            total_hydrogen_produced = []

            for i, vendor in enumerate(vendors):
                electrolyser_input_power = (rectifier_efficiency / 100) * rectifier_input_power
                hydrogen_produced = electrolyser_input_power / rated_powers[i]

                total_electrolyser_input_power.append(np.sum(electrolyser_input_power))
                total_hydrogen_produced.append(np.sum(hydrogen_produced))

            # Plotting Rated Power by Vendor
            st.bar_chart(pd.DataFrame({'Vendor': vendors, 'Rated Power': rated_powers}).set_index('Vendor'))

            # Plotting Total Electrolyser Input Power by Vendor
            st.bar_chart(pd.DataFrame({'Vendor': vendors, 'Total Electrolyser Input Power': total_electrolyser_input_power}).set_index('Vendor'))

            # Plotting Total Hydrogen Produced by Vendor
            st.bar_chart(pd.DataFrame({'Vendor': vendors, 'Total Hydrogen Produced': total_hydrogen_produced}).set_index('Vendor'))
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')
