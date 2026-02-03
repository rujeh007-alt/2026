import streamlit as st
import pandas as pd
import numpy as np
import os
import urllib.request

# --- 1. PAGE CONFIG ---
st.set_page_config(
    page_title="Investment Memo: PROJ-1402", 
    page_icon="🥂", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. IMAGE DOWNLOADER ---
def get_image_path():
    image_path = "gatsby_toast.gif"
    
    # The Great Gatsby Toast - Classy & Perfect for a "Merger"
    url = "https://media.giphy.com/media/8Iv5lqKwKsZ2g/giphy.gif"
    
    if not os.path.exists(image_path):
        try:
            # Download to server so it never breaks
            urllib.request.urlretrieve(url, image_path)
        except:
            return None
    return image_path

# --- 3. SIDEBAR ---
with st.sidebar:
    st.header("🔒 CONFIDENTIAL")
    st.warning("⚠️ RESTRICTED ACCESS")
    st.markdown("---")
    st.markdown("**Deal Code:** VALENTINE-2026")
    st.markdown("**Target Company:** YOU")
    st.markdown("**Analyst:** Rujeh Refaat") 
    st.markdown("**Rating:** STRONG BUY")
    st.markdown("---")
    st.write("© 2026 Institutional Research")

# --- 4. SESSION STATE ---
if 'deal_closed' not in st.session_state:
    st.session_state.deal_closed = False

# --- 5. MAIN APP ---
if not st.session_state.deal_closed:
    st.title("🚀 Strategic Partnership Proposal")
    st.markdown("### Executive Summary: Merger Opportunity")
    st.write("The analyst team (me) has identified a high-synergy opportunity with unlimited upside potential. Immediate execution is recommended.")
    
    # Financial Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projected Happiness", "Infinite", "+100% 🚀")
    col2.metric("Loneliness Risk", "0.00%", "-100% ▼")
    col3.metric("Synergy Rating", "AAA+", "Stable")
    col4.metric("Cost of Capital", "1 Dinner", "Feb 14")

    st.markdown("---")
    
    # Chart
    st.subheader("📈 Historical Performance & Forecast")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Chemistry', 'Vibes', 'Attraction'])
    chart_data['Chemistry'] = chart_data['Chemistry'].cumsum() + 50
    chart_data['Vibes'] = chart_data['Vibes'].cumsum() + 50
    chart_data['Attraction'] = chart_data['Attraction'].cumsum() + 50
    st.line_chart(chart_data)

    st.markdown("---")

    # Buttons
    st.subheader("📝 Investment Committee Decision")
    c1, c2 = st.columns([1, 2])
    
    with c1:
        if st.button("✅ APPROVE MERGER (Yes)", type="primary", use_container_width=True):
            st.session_state.deal_closed = True
            st.rerun()
            
    with c2:
        if st.button("❌ DECLINE DEAL", use_container_width=True):
            st.error("⚠️ ERROR 404: Rejection not found. Hostile takeover initiated. Click Yes. 😉")

else:
    # --- SUCCESS SCREEN ---
    st.balloons()
    st.title("🥂 DEAL CLOSED!")
    st.success("The merger has been approved by the board!")
    
    st.markdown("""
    ### 📂 Next Steps:
    1. **Due Diligence:** Completed.
    2. **Closing Date:** February 14th, 2026.
    3. **Venue:** To be disclosed (I'm picking you up).
    """)
    
    # Show the Gatsby GIF
    img_path = get_image_path()
    if img_path:
        st.image(img_path, caption="Here's to us.")
    else:
        st.write("🥂 CHEERS! (Imagine Leonardo DiCaprio toasting you right now)")