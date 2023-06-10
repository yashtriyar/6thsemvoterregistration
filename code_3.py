# how to create multiple pages or navigation link which can link to another streamlit app or do we have to create one streamlit app and we can give multiple pages in that?


import streamlit as st

def main():
    st.sidebar.title("Navigation")
    page_options = ["Home", "About", "Contact"]
    page_selection = st.sidebar.selectbox("Go to", page_options)

    if page_selection == "Home":
        home_page()
    elif page_selection == "About":
        about_page()
    elif page_selection == "Contact":
        contact_page()
def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")


def about_page():
    st.title("About Page")
    st.write("This is the About Page.")


def contact_page():
    st.title("Contact Page")
    st.write("You can reach us at contact@example.com.")





if __name__ == "__main__":
    main()
