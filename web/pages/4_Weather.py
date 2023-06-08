import streamlit as st
import sys

sys.path.append('/home/geetheswar/Documents/projects/ChatMate')
from weather.helper import Weather


st.header("Weather App")
weather = Weather()
city = st.text_input("Enter the City")
if city:
    weather.set_data(city)
    city = ''
    if weather.is_success():
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="Temperature", value=f"{weather.get_temp()}°C")
        with c2:
            st.write(weather.get_main())
            st.image(weather.get_icon())
