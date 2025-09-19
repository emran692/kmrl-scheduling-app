import streamlit as st

# Import the simulate_what_if function from backend
from backend.what_if_simulation import simulate_what_if

st.title("KMRL What-If Simulation")

st.write("Adjust the train delays to see the updated schedule.")

# --- User Input for Train Delays ---
T1_delay = st.number_input("T1 Delay (minutes)", min_value=0, max_value=60, value=0)
T2_delay = st.number_input("T2 Delay (minutes)", min_value=0, max_value=60, value=0)
T3_delay = st.number_input("T3 Delay (minutes)", min_value=0, max_value=60, value=0)

# --- Run Simulation Button ---
if st.button("Run What-If Simulation"):
    # Prepare conditions dictionary
    conditions = {
        "T1_delay": T1_delay,
        "T2_delay": T2_delay,
        "T3_delay": T3_delay
    }
    
    # Call backend simulation
    updated_schedule = simulate_what_if(conditions)
    
    # Display the results
    st.subheader("Updated Schedule After Simulation")
    for train, time in updated_schedule.items():
        st.write(f"{train}: {time}")
