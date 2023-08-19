import streamlit as st

# Constants for conversion
TPA_TO_KG_YEAR = 1000.00
KG_TO_NM3_YEAR = 11.126
NM3_YEAR_TO_NM3_HR = 8760

def tpa_to_nm3(tpa):
    kg_year = tpa * TPA_TO_KG_YEAR
    nm3_year = kg_year * KG_TO_NM3_YEAR
    nm3_hr = nm3_year / NM3_YEAR_TO_NM3_HR
    return kg_year, nm3_year, nm3_hr

st.title("TPA to NM³/year Converter")

# Input TPA
tpa = st.number_input("Enter the value in TPA:", min_value=0.0)

# Conversion
kg_year, nm3_year, nm3_hr = tpa_to_nm3(tpa)

# Display results
st.write(f"TPA: {tpa}")
st.write(f"KG/year: {kg_year:,.2f}")
st.write(f"NM³/year: {nm3_year:,.2f}")
st.write(f"NM³/hr: {nm3_hr:,.2f}")
