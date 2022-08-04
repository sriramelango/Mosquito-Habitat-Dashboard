import streamlit as st
from PIL import Image
from cv import cnnImageProcessing
import pandas as pd 


st.set_page_config(layout = 'wide')
st.title("CNN Mosquito Habitat Detection")

st.markdown("""
* Dashboard for Global Mosquito Habitat Tracking
* Research conducted at NASA SEES 2021: http://www.tsgc.utexas.edu/sees-internship/
* Title: Autonomous Mosquito Habitat Detection using Satellite Imagery and Convolutional Nueral Networks for Disease Risk Mapping
* Researchers: Sriram Elango, Nandini Ramachandran
* Github: https://github.com/sriramelango/CNN-Mosquito-Detection
* Preprint: https://arxiv.org/abs/2203.04463
* Conference (AGU): https://agu.confex.com/agu/fm21/meetingapp.cgi/Paper/917272

Summary: This research presents an evalutaion of multiple CNN models that aim to autonomously predict the presence of mosquito habitats by running inference on readily available satellite imagery. By determining the locations of potentially dangerous breeding grounds, we can aid in the prevention of the global transmission of mosquito borne vector diseases.
""")

with st.expander("Identify Desired Location"):  
    latitudeInput = st.number_input("Pick your Latitude", min_value = -90.0, max_value = 90.0, step = .1, value = 0.0)
    longitudeInput = st.number_input("Pick your Longitude", min_value = -180.0, max_value=180.0, step = .1, value = 0.0)
    location = pd.DataFrame({"lat": [latitudeInput], "lon": [longitudeInput]})

with st.expander("Location Map Analysis"):
    st.map(location)


image = st.file_uploader("Upload an Image", type= ['png', 'jpg', 'jpeg'])

if image is not None and st.button("Detect"):
    inputImage = Image.open(image)
    with st.spinner('Analyzing...'):
        newImage = Image.open(cnnImageProcessing(inputImage))
        st.image(newImage)