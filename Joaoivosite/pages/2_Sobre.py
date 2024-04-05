import streamlit as st
for k, v in st.session_state.items():
    st.session_state[k] = v

from PIL import Image
import os
path = os.path.dirname(__file__)
my_file = path+'/images/mechub_logo.png'
img = Image.open(my_file)

st.set_page_config(
    page_title='Sobre',
    page_icon=img,
                   )

hide_menu = '''
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        '''
st.markdown(hide_menu, unsafe_allow_html=True)

idioma = st.sidebar.radio(label="",options=["Português", "English"], key="idioma")

if 'active_page' not in st.session_state:
    st.session_state.active_page = '2_Sobre'
    st.session_state.idioma = idioma

if idioma == "English":
    st.header("About me", divider="gray", anchor=False)

    st.markdown('''
    
    I have a degree in Mechanical Engineering. During my academic and professional journey, I've developed an interest in tools that simplify project development.
    
    With experience in CAD and other softwares such as Microsoft Excel, widely used in my field and beyond, I decided to take it a step further. Thus, I aimed to develop my own tools.
    
    Through GitHub, I share Python codes that simplify project development in various areas of Mechanical Engineering, based on theoretical knowledge from books and scientific articles.
    
    Additionally, I eventually post videos on a YouTube channel, demonstrating not only the GitHub codes but also other useful computational tools.
    
    ---
    
    🎓 Graduate degree in Mechanical Engineering at Universidade Federal do Ceará.
    
    🚀 Experience in rocket propulsion.
    
    💨 Two years of experience in HVAC projects.
    
    🔧 Experience in maintenance planning for industrial food machinery.
      '''
                )
    # Download Currículo
    st.divider()

    st.subheader("Contact", divider="gray", anchor=False)
    st.markdown('''

    :email: :blue[joaoivo.rufino@gmail.com]
    
    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jimr/?locale=en_US)

      '''
                )

else:
    st.header("Sobre mim", divider="gray", anchor=False)

    st.markdown('''
    
    Sou graduado em Engenharia Mecânica. No decorrer da minha jornada acadêmica e profissional, desenvolvi interesse por ferramentas que possibilitam agilizar e aprimorar a elaboração de projetos.
    
    Com experiência em CAD e softwares como o Microsoft Excel, amplamente utilizados na minha área e além, decidi avançar ainda mais. Assim, busquei desenvolver minhas próprias ferramentas.
    
    Por meio do GitHub, compartilho códigos em Python que simplificam a elaboração de projetos em diversas áreas da Engenharia Mecânica, embasados em sólida fundamentação teórica proveniente de livros e artigos científicos.
    
    Além disso, eventualmente publico vídeos em um canal do YouTube, demonstrando não apenas os códigos do GitHub, mas também outras ferramentas computacionais amplamente úteis.
    
    ---
    
    🎓 Graduado em Engenharia Mecânica pela Universidade Federal do Ceará.
    
    🚀 Atuação na área de propulsão de foguetes.
    
    💨 Experiência de dois anos em projetos de HVAC (AVAC) e gases.
    
    🔧 Experiência na área de PCM para máquinas industriais do setor alimentício.
      '''
                )

    # Download Resume
    st.divider()

    st.subheader("Contato", divider="gray", anchor=False)
    st.markdown('''

    :email: :blue[joaoivo.rufino@gmail.com]
    
    [![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jimr/)
    
      '''
                )