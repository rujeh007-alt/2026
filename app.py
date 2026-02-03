import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Official Proposal", page_icon="🌹", layout="wide")

# 2. Session State
if 'deal_closed' not in st.session_state:
    st.session_state.deal_closed = False

# 3. Sidebar (Simplified)
with st.sidebar:
    st.info("🔒 **CLASSIFIED DOCUMENT**")
    st.markdown("**Subject:** You & Me")
    st.markdown("**Analyst:** Rujeh Refaat") 
    st.divider()
    st.write("This report analyzes the potential future of us hanging out on Feb 14th.")

# 4. Main Header
if not st.session_state.deal_closed:
    st.title("📊 Strategic Partnership Proposal")
    st.markdown("### Executive Summary: Why we should be technically dating")
    
    # 5. Metrics (Translated to Normal English)
    col1, col2, col3, col4 = st.columns(4)
    # Instead of "Yield", use "Fun Level"
    col1.metric("Predicted Fun", "Maximum", "Off the charts 📈")
    # Instead of "Risk", use "Boredom"
    col2.metric("Boredom Risk", "0.00%", "-100% ▼")
    # Instead of "Synergy", use "Vibe Check"
    col3.metric("Vibe Check", "Immaculate", "Stable")
    # Keep this one, it's funny
    col4.metric("Cost to You", "0 EGP", "I'm Paying")

    # 6. The Chart (Keep it, everyone loves lines going up)
    st.subheader("Projected Happiness Levels")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Laughter', 'Memories', 'Cute Moments']
    )
    chart_data['Laughter'] = chart_data['Laughter'].cumsum() + 50
    chart_data['Memories'] = chart_data['Memories'].cumsum() + 50
    chart_data['Cute Moments'] = chart_data['Cute Moments'].cumsum() + 50
    
    st.line_chart(chart_data)

    st.divider()

    # 7. The Proposal 
    st.subheader("📝 Official Recommendation")
    st.write("Data indicates a 100% probability of a great time.")

    c1, c2 = st.columns([1, 2])
    
    with c1:
        # Clear "YES" button
        if st.button("✅ Accept Offer (Yes)", type="primary", use_container_width=True):
            st.session_state.deal_closed = True
            st.rerun()
            
    with c2:
        # Funny error instead of "Hostile Takeover"
        if st.button("❌ Decline Offer", use_container_width=True):
            st.error("System Error: You are too cute to say no. Please try the other button. 😉")

else:
    # 8. Success Screen
    st.balloons()
    st.title("🎉 IT'S OFFICIAL!")
    st.success("The deal is closed!")
    
    st.markdown("""
    ### The Plan:
    1. **Date:** February 14th
    2. **Activity:** Dinner & vibes
    3. **Dress Code:** Look amazing (as always)
    """)
    
  # This is a more stable link for the 'Wolf of Wall Street' celebration
st.image("my_celebration.gif")



