import streamlit as st
import pandas as pd

average_results = pd.read_csv("average_results_for_the_web_app.csv")
origins = average_results['Origin'].unique()
origin = st.sidebar.selectbox('Depot and Unloading', origins)
destinations = average_results['Destination'].unique()
destination = st.sidebar.selectbox('Loading', destinations)
trucks = average_results['Truck Model'].unique()
truck = st.sidebar.selectbox('Truck Model', trucks)
trailers = average_results['Trailer Model'].unique()
trailer = st.sidebar.selectbox('Trailer', trailers)

cost_per_mile = average_results.loc[(average_results['Origin'] == origin) & \
                        (average_results['Destination'] == destination) & \
                        (average_results['Truck Model'] == truck) & \
                        (average_results['Trailer Model'] == trailer), 'cost_per_mile'].values
assert(len(cost_per_mile)) == 1
cost_per_mile = round(cost_per_mile[0], 4)
print(cost_per_mile)

st.title("Cost per Mile Calculator")
st.write(f"Cost per mile: {cost_per_mile} $/mile")
st.write("")
st.write(f"Depot and Unloading: {origin}")
st.write(f"Loading: {destination}")
st.write(f"Truck Model: {truck}")
st.write(f"Trailer: {trailer}")



