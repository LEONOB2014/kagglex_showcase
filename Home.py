import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.title("Coal Power Plant Estimation based on Satellite Images")

st.info("Click on the left sidebar menu to navigate to the different apps.")

st.subheader("Timelapse of Satellite Imagery")
st.markdown(
    """
    The following timelapse animations were created using the Timelapse web app. Click `Timelapse` on the left sidebar menu to create your own timelapse for any location around the globe.
"""
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://github.com/LEONOB2014/kagglex_showcase/raw/main/animations/termotasajeiro2.gif")
    st.image("https://github.com/LEONOB2014/kagglex_showcase/raw/main/animations/termotasajeiro_1.gif")

with row1_col2:
    st.image("https://github.com/LEONOB2014/kagglex_showcase/raw/main/animations/termozipa.gif")
    st.image("https://github.com/LEONOB2014/kagglex_showcase/raw/main/animations/termozipa.gif")
