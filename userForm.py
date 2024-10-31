import streamlit as st
from datetime import datetime
st.title("User Form")

form_values = {
    "name" : None,
    "age" : None,
    "gender" : None,
    "dob" : None
}

min_date = datetime(1990,1,1)
max_date = datetime.now()

with st.form(key="my_form"):
    form_values["name"] = st.text_input("Enter your name ")
    form_values["age"] = st.number_input("Enter your age")
    form_values["gender"] = st.selectbox("Gender", ['Male', 'Female'])
    form_values["dob"] = st.date_input("Enter your birth date", max_date, min_date)
    submit = st.form_submit_button(label="Submit")

    if submit:
        if not all(form_values.values()):
            st.warning("All field must be filled out!")
        else:
            st.balloons()
            for (key, values) in form_values.items():
                st.write(f"{key} : {values}")
