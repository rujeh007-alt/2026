import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(
    page_title="Investment Memo: PROJ-1402", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Sidebar
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

# 3. Session State
if 'deal_closed' not in st.session_state:
    st.session_state.deal_closed = False

# 4. Main App
if not st.session_state.deal_closed:
    st.title("🚀 Strategic Partnership Proposal")
    st.markdown("### Executive Summary: Merger Opportunity")
    st.write("The analyst team (me) has identified a high-synergy opportunity with unlimited upside potential. Immediate execution is recommended.")
    
    # Metrics
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
    st.title("🎉 DEAL CONFIRMED!")
    st.success("The merger has been approved by the board! Trading is halted for celebration.")
    
    st.markdown("""
    ### 📂 Next Steps:
    1. **Due Diligence:** Completed successfully.
    2. **Closing Date:** February 14th, 2026.
    3. **Venue:** To be disclosed (I'm picking you up).
    4. **Dress Code:** Look amazing (as always).
    """)
    
    # --- THE FIX: RAW HTML ---
    # This forces the browser to load the GIF directly, bypassing Streamlit's blockers.
    st.markdown(
        """
        <div style="display: flex; justify-content: center;">
            <img src="https://media.tenor.com/qW7tHv-F2_gAAAAC/jordan-belfort-leonardo-dicaprio.gif" width="100%" style="max-width: 600px; border-radius: 10px;">
        </div>
        """, 
        unsafe_allow_html=True
    )