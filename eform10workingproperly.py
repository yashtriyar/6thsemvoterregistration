import streamlit as st
from datetime import date, timedelta
import sqlite3
from reportlab.pdfgen import canvas
import os
import base64

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

    # Validation: Check if the date of birth is at least 18 years ago
    min_age_date = date.today() - timedelta(days=365 * 18)
    if dob and dob > min_age_date:
        st.error("You must be at least 18 years old to submit the form.")
        st.stop()

    official_doc = st.file_uploader("Official Document (PDF)", type="pdf")

    disability = st.multiselect("Category of Disability", ("Visual Impairment", "Hearing Impairment",
                                                           "Mobility Impairment", "Intellectual Disability",
                                                           "Psychiatric Disability","None"))

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

        # Generate PDF
        pdf_filename = f"{name}_{surname}_application.pdf"
        generate_pdf(name, surname, relative, applicant_name, applicant_email, relative_name, relative_email,
                     aadhaar, gender, dob, official_doc, disability, pdf_filename)

        st.success("Form submitted successfully!")

        # Download link for the generated PDF
        download_link = create_download_link(pdf_filename)
        st.markdown(download_link, unsafe_allow_html=True)

def generate_pdf(name, surname, relative, applicant_name, applicant_email, relative_name, relative_email,
                 aadhaar, gender, dob, official_doc, disability, filename):
    # Create a PDF using reportlab
    pdf_path = os.path.join(os.getcwd(), filename)
    c = canvas.Canvas(pdf_path)

    # Add form data to the PDF
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, "Name: " + name)
    c.drawString(50, 730, "Surname: " + surname)
    c.drawString(50, 710, "Immediate Relative: " + relative)
    c.drawString(50, 690, "Applicant's Name: " + applicant_name)
    c.drawString(50, 670, "Applicant's Email: " + applicant_email)
    c.drawString(50, 650, "Relative's Name: " + relative_name)
    c.drawString(50, 630, "Relative's Email: " + relative_email)
    c.drawString(50, 610, "Aadhaar Number: " + aadhaar)
    c.drawString(50, 590, "Gender: " + gender)
    c.drawString(50, 570, "Date of Birth: " + str(dob))
    c.drawString(50, 550, "Disability: " + ', '.join(disability))

    # Save the PDF
    c.save()

def create_download_link(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
    base64_pdf = base64.b64encode(file_content).decode('utf-8')
    download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download>Download PDF</a>'
    return download_link

if __name__ == '__main__':
    main()
