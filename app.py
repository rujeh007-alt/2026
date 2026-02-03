import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config (Dark Mode & Professional)
st.set_page_config(
    page_title="Investment Memo: PROJ-1402", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State (Memory)
if 'deal_closed' not in st.session_state:
    st.session_state.deal_closed = False

# 3. Sidebar - The "Analyst Report"
with st.sidebar:
    st.header("🔒 CONFIDENTIAL")
    st.warning("⚠️ RESTRICTED ACCESS")
    st.markdown("---")
    st.markdown("**Deal Code:** VALENTINE-2026")
    st.markdown("**Target Company:** YOU")
    st.markdown("**Analyst:** Rujeh Refaat")  # <--- YOUR NAME IS HERE
    st.markdown("**Rating:** STRONG BUY")
    st.markdown("---")
    st.write("© 2026 Institutional Research")

# 4. Main App Logic
if not st.session_state.deal_closed:
    # --- THE PITCH ---
    st.title("🚀 Strategic Partnership Proposal")
    st.markdown("### Executive Summary: Merger Opportunity")
    st.write("The analyst team (me) has identified a high-synergy opportunity with unlimited upside potential. Immediate execution is recommended.")
    
    # Financial Metrics (The Funny Part)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projected Happiness", "Infinite", "+100% 🚀")
    col2.metric("Loneliness Risk", "0.00%", "-100% ▼")
    col3.metric("Synergy Rating", "AAA+", "Stable")
    col4.metric("Cost of Capital", "1 Dinner", "Feb 14")

    st.markdown("---")

    # The "Stock Chart" (Always going up)
    st.subheader("📈 Historical Performance & Forecast")
    
    # Fake data logic
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Chemistry', 'Vibes', 'Attraction'])
    chart_data['Chemistry'] = chart_data['Chemistry'].cumsum() + 50
    chart_data['Vibes'] = chart_data['Vibes'].cumsum() + 50
    chart_data['Attraction'] = chart_data['Attraction'].cumsum() + 50
    
    st.line_chart(chart_data)

    st.markdown("---")

    # The Decision Buttons
    st.subheader("📝 Investment Committee Decision")
    
    c1, c2 = st.columns([1, 2])
    
    with c1:
        # The YES Button
        if st.button("✅ APPROVE MERGER (Yes)", type="primary", use_container_width=True):
            st.session_state.deal_closed = True
            st.rerun()
            
    with c2:
        # The NO Button (Fake)
        if st.button("❌ DECLINE DEAL", use_container_width=True):
            st.error("⚠️ ERROR 404: Rejection not found. Hostile takeover initiated. You must click Yes. 😉")

else:
    # --- THE SUCCESS SCREEN ---
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
    
    # --- IMAGE HANDLING (NO CRASH GUARANTEE) ---
    try:
        # It looks for a file named 'success.gif'
        st.image("success.gif", caption="Live footage of me right now")
    except:
        # If you forgot to upload the file, it shows this instead of crashing
        st.header("🥂 CHEERS! 🥂")
        st.write("(Imagine Leonardo DiCaprio raising a glass here)")
        