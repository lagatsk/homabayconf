import streamlit as st

# Set the title of the web application with a blue background
st.markdown(
    """
    <style>
    .title {
        font-size: 2.5em;
        color: white;
        background-color: blue;
        padding: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown('<div class="title">Homabay County Best Practice Conference</div>', unsafe_allow_html=True)

# Input fields for user details
name = st.text_input("Enter your name:")
id_number = st.text_input("Enter your ID number:")
phone_number = st.text_input("Enter your phone number:")

# Submit button
if st.button("Submit"):
    if name and id_number and phone_number:
        st.write(f"Name: {name}")
        st.write(f"ID Number: {id_number}")
        st.write(f"Phone Number: {phone_number}")
    else:
        st.write("Please fill in all the fields.")

# Footer comment
st.write("Thank you for attending the Homabay County Best Practice Conference!")
