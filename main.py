import streamlit as st

def canadian_c_spine_rule(age, dangerous_mechanism, paresthesias):
    # Criteria for C-Spine imaging
    if age >= 65:
        return "C-Spine imaging required"
    if dangerous_mechanism:
        return "C-Spine imaging required"
    if paresthesias:
        return "C-Spine imaging required"
    return "C-Spine imaging not required"


st.title("Canadian C-Spine Rule Calculator")
st.write("This app helps determine if a patient requires C-Spine imaging based on the Canadian C-Spine Rule.")

# User input
age = st.number_input("Enter patient's age (in years):", min_value=0, value=0)
dangerous_mechanism = st.checkbox("Was there a dangerous mechanism of injury? (e.g. fall from > 1 meter, axial load to head, high-speed MVA, rollover, ejection, motorized recreational vehicle, bicycle collision)")
paresthesias = st.checkbox("Does the patient have paresthesias in extremities?")

# Calculate and display result
if st.button("Calculate"):
    result = canadian_c_spine_rule(age, dangerous_mechanism, paresthesias)
    st.write("Result:")
    st.write(result)
