import streamlit as st
from datetime import date, timedelta
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import os
import base64


def create_download_link(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
    base64_pdf = base64.b64encode(file_content).decode('utf-8')
    download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download>Download PDF</a>'
    return download_link


def generate_pdf(name, surname, relative, applicant_name, applicant_email, relative_name, relative_email,
                 aadhaar, gender, dob, official_doc, disability, photo, filename):
    pdf_path = os.path.join(os.getcwd(), filename)
    c = canvas.Canvas(pdf_path, pagesize=letter)

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
    c.drawString(50, 550, "Official Document: " + official_doc)
    c.drawString(50, 530, "Disability: " + ", ".join(disability))

    # Add photo to the PDF
    if photo is not None:
        img = Image.open(photo)
        img_width, img_height = img.size
        aspect_ratio = img_height / img_width
        max_width = 200
        img_width = min(max_width, img_width)
        img_height = int(img_width * aspect_ratio)

        img = img.resize((img_width, img_height), Image.ANTIALIAS)
        img_path = os.path.join(os.getcwd(), "temp_photo.png")
        img.save(img_path, format="PNG")

        c.drawImage(img_path, 50, 500, width=img_width, height=img_height)

    # Save the PDF
    c.save()

    return pdf_path


def main():
    st.title("Application Form")

    # Form inputs
    name = st.text_input("Name")
    surname = st.text_input("Surname")

    relatives = ['Father', 'Mother', 'Husband', 'Wife', 'Guardian']
    relative = st.selectbox("Immediate Relative", relatives)

    applicant_name = st.text_input("Applicant's Name")
    applicant_email = st.text_input("Applicant's Email")

    relative_name = st.text_input("Relative's Name")
    relative_email = st.text_input("Relative's Email")

    aadhaar = st.text_input("Aadhaar Number")

    genders = ['Male', 'Female', 'Other']
    gender = st.selectbox("Gender", genders)

    max_date = date.today() - timedelta(days=365 * 18)
    dob = st.date_input("Date of Birth", max_value=max_date)

    official_doc = st.text_input("Official Document")
    disabilities = ['Visual Impairment', 'Hearing Impairment', 'Mobility Impairment', 'Cognitive Impairment']
    disability = st.multiselect("Disability", disabilities)

    photo = st.file_uploader("Upload Photo", type=["jpg", "jpeg", "png"])

    terms = st.checkbox("I agree to the terms and conditions")

    # Submit button
    if terms and st.button("Submit"):
        conn = sqlite3.connect('application.db')
        c = conn.cursor()

        # Create table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS applications
                     (name TEXT, surname TEXT, relative TEXT, applicant_name TEXT, applicant_email TEXT,
                     relative_name TEXT, relative_email TEXT, aadhaar TEXT, gender TEXT, dob DATE,
                     official_doc TEXT, disability TEXT)''')

        # Insert form data into the database
        c.execute("INSERT INTO applications VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (name, surname, relative, applicant_name, applicant_email, relative_name, relative_email,
                   aadhaar, gender, dob, official_doc, ', '.join(disability)))
        conn.commit()
        conn.close()

        pdf_filename = f"{name}_{surname}_application.pdf"
        pdf_path = generate_pdf(name, surname, relative, applicant_name, applicant_email, relative_name,
                                relative_email, aadhaar, gender, dob, official_doc, disability, photo, pdf_filename)

        st.success("Form submitted successfully!")

        # Download link for the generated PDF
        download_link = create_download_link(pdf_path)
        st.markdown(download_link, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
