import streamlit as st

# Set page title and icon
st.set_page_config(page_title="Welcome App", page_icon="👋")

# Create header with welcome message
st.title("👋 Welcome to Our Application!")

# Add some descriptive text
st.markdown("""
### Thanks for visiting our app!

This is a simple welcome page created with Streamlit. Feel free to explore the features below.
""")

# Create a sidebar
st.sidebar.header("Navigation")
st.sidebar.info("Select different sections of the app here")

# Add some interactive elements
if st.button("Click me!"):
    st.balloons()
    st.write("Thanks for clicking! 🎉")

# Add columns for layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("About Us")
    st.write("We're dedicated to creating amazing web applications using Streamlit.")

with col2:
    st.subheader("Contact")
    st.write("📧 Email: example@email.com")
    st.write("📱 Phone: (555) 123-4567")


# Add a footer
st.markdown("---")
st.markdown("### Made with ❤️ using Streamlit")
