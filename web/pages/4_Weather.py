import streamlit as st
import sys

sys.path.append('/home/geetheswar/Documents/projects/ChatMate')
from weather.helper import Weather


def main():
    st.header("Weather App")
    weather = Weather()
    city = st.text_input("Enter the City").lower()
    if st.button("Get Weather Details") and city:
        weather.set_data(city)
        st.write(weather.get_data())
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="Temperature", value=f"{weather.get_temp()}°C")
        with c2:
            st.write(weather.get_main())
            st.image(weather.get_icon())


if __name__ == "__main__":
    main()
