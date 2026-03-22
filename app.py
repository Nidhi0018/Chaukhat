import streamlit as st
import pandas as pd
import pickle
import numpy as np
import base64
import os
from sklearn.preprocessing import LabelEncoder

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Chaukhat | Your Future Home",
    page_icon="🏠",
    layout="wide"
)

# --- 2. IMAGE HANDLING ---
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return None

# Loading local images from your static folder
img_door_base64 = get_image_base64(os.path.join("static", "door.jpeg"))
img_interior_base64 = get_image_base64(os.path.join("static", "interior.jpeg"))
img_motif_base64 = get_image_base64(os.path.join("static", "motif.jpg"))

# --- 3. UI & ANIMATION (CSS) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Inter:wght@400;700&display=swap');

    /* SPLASH SCREEN (Gate Entrance) */
    #splash-screen {{
        position: fixed;
        top: 0; left: 0;
        width: 100vw; height: 100vh;
        background-color: #f7dce0; /* Shared Pearl Pink */
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
        animation: fadeOut 1.2s forwards;
        animation-delay: 3s;
    }}
    .door-frame {{ width: 100vw; height: 100vh; object-fit: cover; position: absolute; }}
    .splash-text {{
        position: absolute; bottom: 80px; width: 100%; color: white;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.7); font-family: 'Cinzel';
        font-size: 2.2rem; letter-spacing: 5px; text-align: center; z-index: 10000;
    }}
    @keyframes fadeOut {{ from {{ opacity: 1; }} to {{ opacity: 0; visibility: hidden; }} }}

    /* MAIN APP BACKGROUND (Pearl Pink) */
    [data-testid="stAppViewContainer"] {{
        background-color: #f7dce0; 
    }}

    /* GLASS HEADER */
    .hero-glass-header {{
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(15px);
        padding: 50px 20px;
        border-radius: 40px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        text-align: center;
        margin: 20px auto 40px auto;
        max-width: 90%;
    }}

    .chaukhat-title {{
        font-family: 'Cinzel', serif !important;
        font-size: 5.5rem !important;
        letter-spacing: 15px;
        color: #2b5968; /* Shared Slate Blue */
        text-transform: uppercase;
        margin: 0;
    }}

    /* THE RESULT CARD - USING YOUR MOTIF BG */
    .result-card {{
        background-image: url("data:image/jpeg;base64,{img_motif_base64}");
        background-size: cover;
        background-position: center;
        padding: 60px 40px;
        border-radius: 40px;
        text-align: center;
        border: 4px solid #2b5968; /* Slate Blue Border */
        box-shadow: 0 30px 60px rgba(43, 89, 104, 0.2);
    }}

    /* INPUT FIELD STYLING */
    label {{ color: #2b5968 !important; font-weight: 700 !important; font-size: 1.2rem !important; }}
    
    div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        color: #2b5968 !important;
        border: 1px solid #cabab1 !important; /* Shared Grey-Taupe */
    }}

    /* BUTTON STYLING */
    .stButton>button {{
        background: linear-gradient(135deg, #2b5968 0%, #97b5c2 100%);
        color: white;
        border-radius: 15px;
        height: 4.5rem;
        font-weight: 700;
        width: 100%;
        border: none;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(43, 89, 104, 0.3);
    }}
    </style>
    
    <div id="splash-screen">
        {f'<img src="data:image/jpeg;base64,{img_door_base64}" class="door-frame">' if img_door_base64 else '<div style="font-size:150px;">🚪</div>'}
        <div class="splash-text">A NEW CHAPTER AWAITS BEHIND THIS DOOR</div>
    </div>
    """, unsafe_allow_html=True)

# --- 4. DATA LOADING ---
@st.cache_resource
def load_assets():
    try:
        model = pickle.load(open('RF_model.pkl', 'rb'))
        classes = np.load('classes.npy', allow_pickle=True)
        le = LabelEncoder()
        le.classes_ = classes
        df = pd.read_csv('cleaned_df.csv')
        return model, le, df
    except: return None, None, None

model, encoder, df = load_assets()

# --- 5. MAIN CONTENT ---
st.markdown("""
    <div class="hero-glass-header">
        <h1 class="chaukhat-title">Chaukhat</h1>
        <p style="color: #2b5968; font-style: italic; font-size: 1.4rem; letter-spacing: 2px; margin-top: 10px;">
            "Opening the Gateway to your future home’s true value"
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div style="max-width: 1350px; margin: auto;">', unsafe_allow_html=True)
col_left, col_right = st.columns([3, 2], gap="large")

with col_left:
    st.markdown("<h2 style='color: #2b5968; font-family: \"Cinzel\";'>🏡 Settle into Comfort</h2>", unsafe_allow_html=True)
    with st.container():
        loc = st.selectbox("Where would you like to build your future?", encoder.classes_ if encoder else ["Data Error"])
        sqft = st.number_input("How much living space do you need? (Sq. Ft.)", 300, 20000, 1500)
        
        st.write("<b style='color:#2b5968;'>Room to Grow</b>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1: bhk = st.selectbox("Bedrooms (BHK)", [1,2,3,4,5,6], index=2)
        with c2: bath = st.selectbox("Bathrooms", [1,2,3,4,5,6], index=2)
        
        st.markdown("<br>", unsafe_allow_html=True)
        analyze_btn = st.button("STEP INSIDE & SEE THE VALUE")

with col_right:
    if analyze_btn and model:
        # Prediction
        loc_id = encoder.transform([loc])[0]
        val = model.predict(np.array([[sqft, bath, bhk, loc_id]]))[0]
        
        # Result Card using Motif Background
        st.markdown(f"""
            <div class="result-card">
                <p style='color: #2b5968; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; opacity: 0.7;'>Fair Market Estimate</p>
                <h1 style='color: #2b5968; font-size: 6rem; margin:0;'>₹ {val:.1f} L</h1>
                <p style='color: #dfc2c0; font-size: 2.2rem; font-weight: 800;'>~ ₹ {(val/100):.2f} Cr</p>
                <hr style='border: 0; border-top: 1px solid rgba(43, 89, 104, 0.2); margin: 35px 0;'>
                <p style='color: #2b5968; font-size: 1.2rem;'><b>Home Location:</b> {loc}</p>
                <p style='color: #10b981; font-weight: bold;'>A Trusted Reflection for your Home</p>
            </div>
        """, unsafe_allow_html=True)
        st.toast("Welcome Home!", icon="✨")
    else:
        st.info("### 🏘️ Your Gateway Awaits")
        if img_interior_base64:
            st.markdown(f'<img src="data:image/jpeg;base64,{img_interior_base64}" style="width:100%; border-radius:30px; box-shadow: 0 20px 40px rgba(0,0,0,0.2);">', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("---")
st.caption("Chaukhat 2026 | Helping you step into the home you've always dreamed of.")