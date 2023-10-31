import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


# Customize page title
st.title("Coal Power Plant Estimation based on Satellite Images")


st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)