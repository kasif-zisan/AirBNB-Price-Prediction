import streamlit as st
import pickle

# Load the pickled model
model = pickle.load(open("gb_reg.pkl", "rb"))

# Define input fields with appropriate labels and types
st.title("NYC Airbnb Price Prediction")

minimum_nights = st.number_input("Minimum Nights", value=1, min_value=1)
calculated_host_listings_count = st.number_input("Calculated Host Listings Count", value=0)
availability_365 = st.number_input("Availability 365", value=0)

neighbourhood_group = st.selectbox("Neighbourhood Group",
                                   ["Bronx", "Brooklyn", "Manhattan", "Queens", "Staten Island"])
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])

# Map encoded values for neighbourhood_group and room_type
neighbourhood_group_mapping = {
    "Bronx": 0,
    "Brooklyn": 1,
    "Manhattan": 2,
    "Queens": 3,
    "Staten Island": 4
}
room_type_mapping = {
    "Entire home/apt": 0,
    "Private room": 1,
    "Shared room": 2
}

# Preprocess input data
features = [
    minimum_nights,
    calculated_host_listings_count,
    availability_365,
    neighbourhood_group_mapping[neighbourhood_group],
    room_type_mapping[room_type]
]

# Make prediction when button is clicked
if st.button("Predict Price"):
    predicted_price = model.predict([features])[0]
    st.write("Predicted Price: $", predicted_price)
