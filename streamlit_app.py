import streamlit as st

# Define valid credentials
valid_username = "abcd"
valid_password = "1234"

# Locations
locations = ["Roorkee", "Kurukshetra", "Greater Noida", "Vikas Nagar", "Saharanpur"]

# Title
st.markdown(
    f"""
    <div style="text-align: center; background-color: #f4f4f4; border-radius: 10px; padding: 20px;">
        <h1 style="font-size: 32px; color: black; font-weight: bold; font-family: Georgia;">Exploratory Data Analysis</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Sidebar for login
st.sidebar.header("Login")

# Input fields for username and password
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Check credentials and show content if correct
if st.sidebar.button("Login"):
    if username == valid_username and password == valid_password:
        st.success("Login successful! You can access the content.")
        
        # Dropdown menu for locations
        selected_location = st.selectbox("Select a Location", locations)
        
        # Add your content based on the selected location
        st.write(f"You have selected the location: {selected_location}")
    else:
        st.error("Invalid credentials. Please try again.")
