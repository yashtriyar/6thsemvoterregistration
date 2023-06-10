import streamlit as st

# Title of the app
st.title('Simple Form')

# Create a form object
form = st.form(key='my_form')

# Add some text to the form
form.markdown('Please enter your name, email, and favorite color.')

# Add some input fields to the form
name = form.text_input(label='Name')
email = form.text_input(label='Email')
color = form.selectbox(label='Favorite color', options=['Red', 'Green', 'Blue'])

# Add a submit button to the form
submit_button = form.form_submit_button(label='Submit')

# Display the results of the form submission
if submit_button:
    st.write(f'Hello {name}, your email is {email}, and your favorite color is {color}.')
