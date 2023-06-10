import streamlit as st
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('form_data.db')
c = conn.cursor()

# Create a table to store form data
c.execute('''CREATE TABLE IF NOT EXISTS form_data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              surname TEXT,
              relative TEXT,
              applicant_name TEXT,
              applicant_email TEXT,
              relative_name TEXT,
              relative_email TEXT,
              aadhaar TEXT,
              gender TEXT,
              dob TEXT,
              official_doc BLOB,
              disability TEXT)''')

# Streamlit app
def main():
    st.title("Application Form")

    # Form inputs
    name = st.text_input("Name")
    surname = st.text_input("Surname")

    relative = st.selectbox("Immediate Relative", ("Father", "Mother", "Husband", "Wife", "Guardian"))

    applicant_name = st.text_input("Applicant's Name")
    applicant_email = st.text_input("Applicant's Email")

    relative_name = st.text_input("Relative's Name")
    relative_email = st.text_input("Relative's Email")

    aadhaar = st.text_input("Aadhaar Number")

    gender = st.radio("Gender", ("Male", "Female", "Third Gender"))

    dob = st.date_input("Date of Birth")

    official_doc = st.file_uploader("Official Document (PDF)", type="pdf")

    disability = st.multiselect("Category of Disability", ("Visual Impairment", "Hearing Impairment",
                                                           "Mobility Impairment", "Intellectual Disability",
                                                           "Psychiatric Disability"))

    terms = st.checkbox("I agree to the terms and conditions")

    # Submit button
    if terms and st.button("Submit"):
        # Store form data in the database
        c.execute('''INSERT INTO form_data (name, surname, relative, applicant_name, applicant_email,
                     relative_name, relative_email, aadhaar, gender, dob, official_doc, disability)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (name, surname, relative, applicant_name, applicant_email, relative_name,
                   relative_email, aadhaar, gender, dob, official_doc.read() if official_doc else None,
                   ', '.join(disability)))
        conn.commit()

        st.success("Form submitted successfully!")

if __name__ == '__main__':
    main()
