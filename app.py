import streamlit as st
import random
import time

# --- এখানে তোমার Password সেট করো ---
MY_PASSWORD = "R15M2026" 

st.set_page_config(page_title="Pro Signal App", page_icon="🔥")

# --- Login System ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 Private Signal App")
    st.write("Login করতে Password দাও")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if pwd == MY_PASSWORD:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("ভুল Password!")
    st.stop()

# --- Login এর পর ভিতরের অংশ ---
st.title("🔥 Quotex Pro Signal - 1 Min")
st.success("Login Success!")

market = st.selectbox("Market Select করো", ["EURUSD_otc", "EURUSD", "GBPUSD_otc", "Real Market All"])

if st.button("Signal Start করো"):
    placeholder = st.empty()
    for i in range(100):
        # এখানে পরে তোমার real indicator logic বসবে
        signal = random.choice(["UP ⬆️", "DOWN ⬇️", "WAIT ⏳"])
        color = "green" if "UP" in signal else "red" if "DOWN" in signal else "gray"
        
        with placeholder.container():
            st.markdown(f"<h1 style='color:{color}; text-align:center;'>{market} : {signal}</h1>", unsafe_allow_html=True)
            st.write(f"Time: {time.strftime('%H:%M:%S')}")
        time.sleep(3)

if st.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()
