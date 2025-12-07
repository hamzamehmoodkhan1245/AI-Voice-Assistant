import streamlit as st
from streamlit_folium import folium_static
import folium


st.set_page_config(layout="wide", page_title="AI Voice Assistant", page_icon='🎙️')
st.title("Sino-Pak Center Of AI (SPCAI)")

# ------------------------------
#  Project Description 
# ------------------------------
st.markdown("""
<p style="font-size:1.1rem; line-height:1.7; color:#EAEAEA;">
The <strong>Sino-Pak Center of Artificial Intelligence (SPCAI)</strong> is a dedicated research and innovation hub focused on 
advancing Artificial Intelligence education and applied research at the 
<em>Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST), Haripur</em>.
</p>

<p style="font-size:1.1rem; line-height:1.7; color:#EAEAEA;">
This center fosters cutting-edge research and innovation in Artificial Intelligence (AI), 
Machine Learning (ML), Robotics, and Data Science. It aims to bridge the gap between academia 
and industry by promoting collaborative development of AI-driven solutions that contribute 
to Pakistan’s technological growth and global competitiveness.
</p>

<p style="font-size:1.1rem; line-height:1.7; color:#EAEAEA;">
The <strong>AI Voice Assistant</strong> project is one of the significant research initiatives under SPCAI, 
developed collaboratively by <strong>Hamza Haroon</strong> and <strong>Sidra Khan</strong> from the 
<strong>Department of Artificial Intelligence</strong>, 
<em>Pak-Austria Fachhochschule Institute of Applied Sciences and Technology, Haripur</em>.
This system enables intelligent, natural, and voice-based human-computer interaction 
through AI-powered voice recognition and contextual response generation.
</p>

<p style="font-size:1.1rem; line-height:1.7; color:#EAEAEA;">
For more information, visit the 
<a href="https://github.com/hamzamehmoodkhan1245/AI-Voice-Assistant" target="_blank" style="color:#4FC3F7; text-decoration:none;">
SPCAI official website
</a>.
</p>
""", unsafe_allow_html=True)

# ------------------------------
# Vision Section
# ------------------------------
st.subheader("Our Vision")
st.write('''To become a leading center for AI-related research in the region 
by making impactful research contributions in the field of Artificial Intelligence and Machine Learning.''')

# ------------------------------
# Mission Section
# ------------------------------
st.subheader("Our Mission")
st.write('''To nurture talent and create an ecosystem of innovation across all areas related 
to AI and Machine Learning, through active collaboration with academia, industry, and society. 
To conduct impactful applied research and foster strong academic–industry synergy for AI adoption.''')

# ------------------------------
# Research Groups
# ------------------------------
st.subheader("Research Groups and Areas of Interest")
st.markdown("""
The following research groups within SPCAI conduct fundamental and applied research in their respective domains:
- Deep Learning / Machine Learning Research Group  
- Data Science Research Group  
- Robotics and Machine Vision Research Group  
- NLP and Speech Recognition Research Group  
- Evolutionary Computation Research Group
""")

# ------------------------------
# Location Section
# ------------------------------
st.subheader("SPCAI Location")
st.markdown('**Haripur, Pakistan**')
st.markdown("**Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)**")
st.markdown("**Department of Artificial Intelligence Building**")

# ------------------------------
# Map Section
# ------------------------------
m = folium.Map(location=[33.909168, 72.918026], zoom_start=16)
tooltip = "Sino-Pak Center Of AI (SPCAI)"
folium.Marker(
    [33.909168, 72.918026],
    popup="Sino-Pak Center Of AI (SPCAI)",
    tooltip=tooltip
).add_to(m)

# Render Folium Map in Streamlit
folium_static(m)
