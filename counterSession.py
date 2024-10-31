import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Incresement Counter"):
    st.session_state.count += 1
    st.write(f'Counter incresement to {st.session_state.count}')

if st.button("Reset"):
    st.session_state.count = 0

st.write(f'Curr counter -> {st.session_state.count}')
