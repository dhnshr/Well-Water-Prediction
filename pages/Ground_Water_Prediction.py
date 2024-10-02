import streamlit as st
import pandas as pd
import pickle

# Load the machine learning model
model_file_path = './Model/random_forest_model.pkl'
with open(model_file_path, 'rb') as file:
    model = pickle.load(file)

dataset_path = './Data/Current_Draft.csv'
df = pd.read_csv(dataset_path)

# Define function to calculate well depth based on total extraction
def calculate_well_depth(total_extraction):
    if total_extraction < 10000:
        return 112
    elif total_extraction >= 15000 and total_extraction < 17000:
        return 141
    elif total_extraction >= 17000:
        return 157
    else:
        # For other cases, return a default value
        return 0  # You can adjust this default value as needed

# Streamlit app title
st.title("Current Water Level with NAQUIM data")
districts = {
    # Define district data as before
}

# Define input columns
col1, col2 = st.columns(2)  # Create two columns

with col1:
    # Add a drop-down box for selecting the state
    name_of_state = st.selectbox('Select State', df['Name of State'].unique())
    selected_district = st.selectbox('Select District', df[df['Name of State'] == name_of_state]['Name of District'].unique())
    recharge_from_rainfall_monsoon = st.text_input('Recharge from rainfall During Monsoon Season')
    recharge_from_other_sources_monsoon = st.text_input('Recharge from other sources During Monsoon Season')

with col2:
    recharge_from_rainfall_non_monsoon = st.text_input('Recharge from rainfall During Non Monsoon Season')
    recharge_from_other_sources_non_monsoon = st.text_input('Recharge from other sources During Non Monsoon Season')
    total_natural_discharges = st.text_input('Total Natural Discharges')

# Button to trigger prediction
if st.button('Total Extractable Ground Water resource'):
    # Check if all input fields are filled
    if not recharge_from_rainfall_monsoon or not recharge_from_other_sources_monsoon or not recharge_from_rainfall_non_monsoon or not recharge_from_other_sources_non_monsoon or not total_natural_discharges:
        st.warning("Please enter values for all input fields.")
    else:
        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'Recharge from rainfall During Monsoon Season': [float(recharge_from_rainfall_monsoon)],
            'Recharge from other sources During Monsoon Season': [float(recharge_from_other_sources_monsoon)],
            'Recharge from rainfall During Non Monsoon Season': [float(recharge_from_rainfall_non_monsoon)],
            'Recharge from other sources During Non Monsoon Season': [float(recharge_from_other_sources_non_monsoon)],
            'Total Natural Discharges': [float(total_natural_discharges)],
        })

        # Make predictions using the loaded model
        water_level_prediction = model.predict(input_data)

        # Display results
        st.success(f"Total Extractable Ground Water resource: {water_level_prediction[0]:.2f}")

        filtered_df = df[(df['Name of State'] == name_of_state) & (df['Name of District'] == selected_district)]

        if filtered_df.empty:
            st.info(f"Data not found for the given state and district {name_of_state} and {selected_district}.")
        else:
            # Get the total current annual ground water extraction
            total_extraction = filtered_df['Total Current Annual Ground Water Extraction'].values[0]
            st.info(f"Total Current Annual Ground Water Extraction for {name_of_state}, {selected_district}: {total_extraction:.2f}")

            # Calculate the stage of ground water extraction
            stage_extraction = (total_extraction / water_level_prediction[0]) * 100
            st.info(f"Stage of Ground Water extraction: {stage_extraction:.2f}%")

            # Calculate well depth based on total extraction
            well_depth = calculate_well_depth(total_extraction)
            st.info(f"Suggested well depth: {well_depth} meters")
