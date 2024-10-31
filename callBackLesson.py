import streamlit as st

if "part" not in st.session_state:
    st.session_state.part = 1

if "info" not in st.session_state:
    st.session_state.info = {}

def moveToPart2(name):
    st.session_state.info["name"] = name 
    st.session_state.part = 2

if st.session_state.part == 1:
    st.header("Part 1: Form Submission!")
    name = st.text_input("Enter your name", value=st.session_state.info.get("name",""))
    st.button("Next", on_click=moveToPart2, args=(name,))

elif st.session_state.part == 2:
    st.header("Part 2: Review!")
    st.write("Pls review this:")
    st.write(f"**Name**: {st.session_state.info.get('name','')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
