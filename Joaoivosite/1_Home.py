import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

import plotly.graph_objects as go

import streamlit as st
st.session_state.update(st.session_state)
for k, v in st.session_state.items():
    st.session_state[k] = v

from PIL import Image
import os
path = os.path.dirname(__file__)
my_file = path+'/pages/images/mechub_logo.png'
img = Image.open(my_file)

st.set_page_config(
    page_title='Home',
    page_icon=img
                   )

hide_menu = '''
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
'''
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .st-emotion-cache-ch5dnh
    {
        visibility: hidden;
    }
    .st-emotion-cache-q16mip
    {
        visibility: hidden;
    }
    .st-emotion-cache-ztfqz8
    {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if 'active_page' not in st.session_state:
    st.session_state.active_page = '1_Home'
    st.session_state.idioma = "Português"

idioma = st.sidebar.radio(label="",options=["Português", "English"], key="idioma")

if idioma == "English":

    st.header("Social Media", divider="gray", anchor=False)
    st.markdown('''

    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jimr/)  [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Mechub?sub_confirmation=1)  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GitMechub)
    
      '''
                )

    st.header("Tools", divider="gray", anchor=False)

    st.subheader("HVAC Duct Sizing", divider="gray", anchor=False)

    #   HVAC Duct sizing
    path1 = os.path.dirname(__file__)
    my_file1 = path1 + '/pages/images/Thumb_Mechub_2.png'
    img1 = Image.open(my_file1)

    st.image(img1)

    st.link_button("🔧 Tool", "https://github.com/GitMechub/HVAC-Duct_Sizing")
    st.link_button("🎞️ Tutorial video", "https://www.youtube.com/watch?v=FLz8qtGiTjw")

    #   Rocket nozzle sizing
    st.subheader("Rocket Nozzle Sizing", divider="gray", anchor=False)

    path2 = os.path.dirname(__file__)
    my_file2 = path2 + '/pages/images/Thumb_Mechub.png'
    img2 = Image.open(my_file2)

    st.image(img2)

    st.link_button("🔧 Tool", "https://github.com/GitMechub/Rocket-Nozzle_Sizing")
    st.link_button("📱 App", "https://rocketnozzlesizing.streamlit.app/")
    st.link_button("🎞️ Tutorial video", "https://www.youtube.com/watch?v=Crxc9OeuSTg")
    st.link_button("🎞️ Tutorial video (CAD)", "https://www.youtube.com/watch?v=XwzFDo7mbuQ&t=4s")

    #   Rocket centrifugal pump sizing
    st.subheader("Rocket Centrifugal Pump Sizing", divider="gray", anchor=False)

    path3 = os.path.dirname(__file__)
    my_file3 = path3 + '/pages/images/Thumb_Mechub_3.png'
    img3 = Image.open(my_file3)

    st.image(img3)

    st.link_button("🔧 Tool", "https://github.com/GitMechub/Rocket-Centrifugal_Pump")

else:

    st.header("Redes Sociais", divider="gray", anchor=False)

    st.markdown('''

    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jimr/) [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@Mechub?sub_confirmation=1)  [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GitMechub)

      '''
                )

    st.header("Ferramentas", divider="gray", anchor=False)

    st.subheader("Dimensionamento de Dutos AVAC", divider="gray", anchor=False)

    #   HVAC Duct sizing
    path1 = os.path.dirname(__file__)
    my_file1 = path1 + '/pages/images/Thumb_Mechub_2.png'
    img1 = Image.open(my_file1)

    st.image(img1)

    st.link_button("🔧 Ferramenta", "https://github.com/GitMechub/HVAC-Duct_Sizing")
    st.link_button("🎞️ Vídeo tutorial", "https://www.youtube.com/watch?v=FLz8qtGiTjw")

    #   Rocket nozzle sizing
    st.subheader("Dimensionamento de Bocal de Foguete", divider="gray", anchor=False)

    path2 = os.path.dirname(__file__)
    my_file2 = path2 + '/pages/images/Thumb_Mechub.png'
    img2 = Image.open(my_file2)

    st.image(img2)

    st.link_button("🔧 Ferramenta", "https://github.com/GitMechub/Rocket-Nozzle_Sizing")
    st.link_button("📱 App", "https://rocketnozzlesizing.streamlit.app/")
    st.link_button("🎞️ Vídeo tutorial", "https://www.youtube.com/watch?v=Crxc9OeuSTg")
    st.link_button("🎞️ Vídeo tutorial (CAD)", "https://www.youtube.com/watch?v=XwzFDo7mbuQ&t=4s")

    #   Rocket centrifugal pump sizing
    st.subheader("Dimensionamento de Bomba Centrífuga de Foguete", divider="gray", anchor=False)

    path3 = os.path.dirname(__file__)
    my_file3 = path3 + '/pages/images/Thumb_Mechub_3.png'
    img3 = Image.open(my_file3)

    st.image(img3)

    st.link_button("🔧 Ferramenta", "https://github.com/GitMechub/Rocket-Centrifugal_Pump")



