# =======================================
# AI Voice Assistant - Streamlit App (Dark Professional Edition)
# Developed by Hamza Haroon & Sidra Khan
# Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)
# =======================================

import streamlit as st
from PIL import Image
import io
import base64

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------
# Global Dark Theme Professional Styling
# ------------------------------
st.markdown("""
<style>
/* Main background and font */
body, div, p, li, span, label {
    font-family: 'Poppins', 'Segoe UI', sans-serif;
    color: #F0F0F0 !important; /* Bright white-gray text */
    font-size: 1.07rem !important;
}

/* Background colors */
main {
    background-color: #0E1117; /* Streamlit dark gray background */
}

/* Content container with card styling */
.block-container {
    background-color: #11151C;
    border-radius: 12px;
    padding: 25px 35px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.6);
}

/* Headings with glowing gradient */
h1, h2, h3, h4 {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(90deg, #66CCFF, #1E90FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
}

/* Subheadings */
h5, h6 {
    color: #66B2FF !important;
    font-weight: 600;
}

/* Paragraphs */
p {
    color: #DDDDDD !important;
    line-height: 1.7;
}

/* Lists */
ul {
    line-height: 1.8;
    color: #E0E0E0;
}

/* Tabs text */
[data-testid="stTabs"] button div p {
    color: #66CCFF !important;
    font-weight: 600;
}

/* Links */
a {
    color: #4DB8FF !important;
    text-decoration: none;
}
a:hover {
    color: #66CCFF !important;
    text-decoration: underline;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #11151C !important;
    border-right: 1px solid #2C2F36;
}
section[data-testid="stSidebar"] * {
    color: #F0F0F0 !important;
    font-weight: 500 !important;
}
section[data-testid="stSidebar"] svg {
    fill: #66CCFF !important; /* Sidebar icons color */
}

/* Horizontal line */
hr {
    border: none;
    height: 1px;
    background-color: #333;
    margin: 25px 0;
}

/* Cover title and subtitle */
.cover-title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: bold;
    background: linear-gradient(90deg, #00BFFF, #1E90FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.cover-subtitle {
    text-align: center;
    font-size: 1.3rem;
    color: #CCCCCC;
    margin-top: -10px;
    font-weight: 500;
}

/* Cover image */
.cover-img {
    display: block;
    margin-left: auto;
    margin-right: auto;
    max-width: 85%;
    height: auto;
    border-radius: 15px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.6);
}

/* Feature boxes */
.stColumn {
    background-color: #161B22;
    border-radius: 10px;
    padding: 15px;
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.4);
}

/* Streamlit alerts */
.stAlert {
    background-color: #1C1F26;
    border-left: 5px solid #007ACC;
    border-radius: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #BBBBBB;
    font-size: 0.95rem;
    margin-top: 25px;
}
.footer strong {
    color: #66CCFF;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Utility: convert image to base64 for HTML embedding
# ------------------------------
def image_to_base64(img_path):
    img = Image.open(img_path)
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# ------------------------------
# Cover Image Section
# ------------------------------
with st.container():
    st.markdown('<h1 class="cover-title">AI Voice Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="cover-subtitle">Developed by Hamza Haroon & Sidra Khan at PAF-IAST</p>', unsafe_allow_html=True)

    cover_img_path = "cover.png"
    try:
        st.markdown(f'<img class="cover-img" src="data:image/png;base64,{image_to_base64(cover_img_path)}"/>', unsafe_allow_html=True)
    except:
        st.warning("⚠️ Cover image not found. Please place 'cover.png' in your app folder.")

st.markdown("<hr>", unsafe_allow_html=True)

# ------------------------------
# About Project Section
# ------------------------------
with st.container():
    st.subheader("Project Description")
    st.markdown(
        """
        <p>
        <strong>AI Voice Assistant</strong> is a smart, interactive system capable of understanding natural speech and responding intelligently.
        The assistant leverages cutting-edge AI technologies, including dialogue preprocessing, fuzzy and exact matching algorithms, and real-time voice-to-text & text-to-speech conversion.
        </p>

        <p>
        This project was collaboratively developed by <strong>Hamza Haroon</strong> and <strong>Sidra Khan</strong> at the  
        <em>Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)</em>.
        </p>
        """,
        unsafe_allow_html=True
    )

# ------------------------------
# Methodology Section with Tabs
# ------------------------------
with st.container():
    st.subheader("Methodology & Tools")
    tab1, tab2 = st.tabs(["🧠 Methodology", "🧩 Tools Used"])

    with tab1:
        st.markdown("""
        <ul>
            <li><strong>Data Preprocessing</strong>: Cleaned and structured dialogue datasets for model training.</li>
            <li><strong>Matching Algorithms</strong>: Implemented fuzzy and exact matching to improve query understanding.</li>
            <li><strong>Voice Integration</strong>: Converts real-time voice input to text and text back to speech.</li>
            <li><strong>Machine Learning Models</strong>: Utilized LSTM and Transformer models for contextual understanding.</li>
            <li><strong>Collaboration & Version Control</strong>: Managed the project via GitHub for version tracking.</li>
        </ul>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <ul>
            <li><strong>NLP Libraries</strong>: Used NLTK for natural language processing.</li>
            <li><strong>Fuzzy & Exact Matching</strong>: Enhanced query accuracy and response retrieval.</li>
            <li><strong>Pandas</strong>: For data manipulation and performance monitoring.</li>
            <li><strong>Streamlit</strong>: Created a responsive and interactive web-based GUI.</li>
            <li><strong>GitHub</strong>: Collaboration, version control, and continuous updates.</li>
        </ul>
        """, unsafe_allow_html=True)

# ------------------------------
# Features Highlight Section
# ------------------------------
with st.container():
    st.subheader("Key Features")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**🎤 Voice Input:** Smooth real-time speech recognition and conversion to text.")
    with c2:
        st.markdown("**🤖 Intelligent Responses:** Context-aware AI-generated responses.")
    with c3:
        st.markdown("**📊 Analytics:** View performance metrics and user interaction insights.")

# ------------------------------
# Footer
# ------------------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    """
    <p class="footer">
    &copy; 2025 <strong>Hamza Haroon</strong> & <strong>Sidra Khan</strong><br>
    Pak-Austria Fachhochschule Institute of Applied Sciences and Technology (PAF-IAST)
    </p>
    """,
    unsafe_allow_html=True
)
