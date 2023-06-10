import streamlit as st

def app():
    st.title("Application for Inclusion in Electoral Roll")
    st.header("To,")
    st.write("The Electoral Registration Officer,")
    st.write("No. & Name of Assembly Constituency: [Enter Constituency Number and Name]")
    st.write("Or No. & Name of Parliamentary Constituency: [Enter Constituency Number and Name]")
    st.write("(@ only for Union Territories not having Legislative Assembly)")
    st.write("")
    st.write("I submit an application for the inclusion of my name in the electoral roll for the above constituency.")
    st.write("")

    st.subheader("(1)(a) Name (In Official Language of State)")
    first_name = st.text_input("First Name followed by Middle Name")
    surname = st.text_input("Surname (if any)")

    st.subheader("(1)(b) Name (In English in BLOCK LETTERS)")
    first_name_en = st.text_input("First Name followed by Middle Name")
    surname_en = st.text_input("Surname (if any)")

    st.subheader("Disclaimer")
    st.write("If the name is not filled in English, it will be transliterated by software.")

    st.subheader("(2)(a) Name and Surname (in the official language of State) of any one of the relatives:")
    relative_name = st.text_input("Name")
    relative_surname = st.text_input("Surname (if any)")

    st.subheader("(2)(b) Name and Surname (In English in BLOCK LETTERS) of the relative mentioned above")
    relative_name_en = st.text_input("Name")
    relative_surname_en = st.text_input("Surname (if any)")

    st.subheader("(3) Mobile No.")
    mobile_no = st.text_input("Mobile No. of Self (if available) or of relative mentioned at Item No. 2")

    st.subheader("(4) Email ID")
    email = st.text_input("Email ID of Self (If available) or of relative mentioned at Item No. 2")

    st.subheader("(5) Aadhaar Details")
    aadhaar_options = ["Aadhaar Number", "I don't have Aadhaar Number"]
    aadhaar_choice = st.selectbox("Please tick the appropriate box", aadhaar_options)

    st.subheader("(6) Gender")
    gender_options = ["Male", "Female", "Third Gender"]
    gender = st.selectbox("Gender", gender_options)

    st.subheader("(7)(a) Date of Birth")
    dob = st.date_input("Date of Birth")

    st.subheader("(7)(b) Self-attested copy of document supporting age proof attached")
    age_proof_options = [
        "Birth certificate issued by Competent Local Body/Municipal Authority/Registrar of Births & Deaths",
        "Aadhaar Card",
        "PAN Card",
        "Driving License",
        "Certificates of Class X or Class XII issued by CBSE/ICSE/State Education Boards, if it contains Date of Birth",
        "Indian Passport",
        "Any Other Document for Proof of Date of Birth (Pl. Specify)"
    ]
    age_proof_choice = st.selectbox("Document for Proof of Date of Birth", age_proof_options)

    st.subheader("(8)(a) Present Ordinary Residence (Full Address)")
    address = st.text_area("Complete postal address with PIN code")

    st.subheader("(8)(b) Self-attested copy of address proof")
    address_proof_options = [
        "Water/Electricity/Gas connection Bill for.
