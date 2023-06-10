import streamlit as st

def app():
    st.title("Voter Registration Form")

    st.header("To:")
    st.write("The Electoral Registration Officer,")
    st.text_input("No. & Name of Assembly Constituency No. Name")
    st.text_input("Or No. & Name of Parliamentary Constituency@ No. Name")
    st.write("(@ only for Union Territories not having Legislative Assembly)")

    st.header("I submit application for inclusion of my name in the electoral roll for the above constituency.")

    st.subheader("(1)(a) Name (In Official Language of State)")
    st.text_input("First Name followed by Middle Name")
    st.write("SPACE FOR PASTING")
    st.write("ONE RECENT")
    st.write("UNSIGNED PASSPORT")
    st.write("SIZE COLOR")
    st.write("PHOTOGRAPH (4.5 CM")
    st.write("X 3.5 CM) SHOWING")
    st.write("FRONTAL VIEW OF")
    st.write("FULL FACE WITH")
    st.write("WHITE BACKGROUND")
    st.text_input("Surname (if any)")

    st.subheader("(1)(b) Name (In English in BLOCK LETTERS)")
    first_name_en = st.text_input("First Name followed by Middle Name", key="first_name_en")
    st.text_input("Surname (if any)", key="surname_en")

    st.subheader("Disclaimer: If name not filled in English, it will be transliterated by software.")

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
        "Water/Electricity/Gas connection Bill for that address (at least 1 year)",
        "Aadhaar Card",
        "Current passbook of Nationalized/Scheduled Bank/Post Office",
        "Indian Passport",
        "Revenue Department's Land Owning records including Kisan Bahi",
        "Registered Rent Lease Deed (In case of tenant)",
        "Registered Sale Deed (In case of own house)",
        "Any Other document for Proof of residence (Pl. Specify)"
    ]
    address_proof_choice = st.selectbox("Document for proof of residence", address_proof_options)

    st.subheader("(9) Category of disability (Optional)")
    disability = st.text_input("Category of disability")
    percentage_disability = st.number_input("Percentage of disability", min_value=0, max_value=100)
    disability_certificate = st.checkbox("Certificate attached")

    st.subheader("(10) Details of family member already included in the electoral roll")
    family_name = st.text_input("Name of family member")
    family_relationship = st.text_input("Relationship with applicant")
    family_epic = st.text_input("EPIC no.")

    st.subheader("DECLARATION")
    st.write("I HEREBY DECLARE that to the best of my knowledge and belief:")
    st.write("(i) I am a citizen of India and place of my birth is:")
    birth_village = st.text_input("Village/Town")
    birth_district = st.text_input("District")
    birth_state = st.text_input("State/UT")
    st.write("(ii) I am ordinarily a resident at the address mentioned at Sr. No. 8(a) in Form 6 since (mention month and year)")
    residence_since = st.text_input("Residence since (Month and Year)")
    st.write("(iii) I am applying for inclusion in the Electoral Roll for the first time and my name is not included in any Assembly Constituency/Parliamentary Constituency.")
    st.write("(iv) I don't possess any of the mentioned documents for proof of Date of Birth/Age. Therefore, I have enclosed [Name of the document] in support of age proof (Strike off, if not applicable).")
    st.write("(v) I am aware that making the above statement or declaration in relation to this application which is false and which I know or believe to be false or do not believe to be true, is punishable under Section 31 of the Representation of the People Act, 1950 (43 of 1950) with imprisonment for a term which may extend to one year or with fine or with both.")
    st.write("")

    st.subheader("Acknowledgement/Receipt for application")
    st.write("Acknowledgment Number:")
    st.write("Date:")
    st.write("Received the application in Form 6 of Shri/Smt./Ms.")
    st.write("[Applicant can refer the Acknowledgement No. to check the status of the application.]")
    st.write("Name/Signature of ERO/AERO/BLO")
    st.write("")
    st.write("To be appended to Form-6")
    st.write("(The fields marked with * are mandatory)")
    st.write("")
    st.write("GUIDELINES FOR FILLING UP THE APPLICATION FORM-6")
    st.write("1. General Instructions:")
    st.write("(a) The application will be addressed to the Electoral Registration Officer(ERO) of the Assembly Constituency (AC)/Parliamentary Constituency(PC) in which the applicant is ordinarily residing. In case the applicant does not know or has any doubt about the number and name of Assembly Constituency / Parliamentary Constituency, assistance may be extended by the Electoral Registration Officer, and the application will not be rejected on the ground of not mentioning the number and name of Assembly Constituency / Parliamentary Constituency.")
    st.write("(b) The applicant can fill entries of the application either in English or the official language of the state, and this will not be a ground for rejection of the application.")
    st.write("(c) A service personnel, applying for enrolment as a general elector in the electoral roll at his place of posting at a peace station, should ensure that he is not already enrolled as a service elector or general elector in some other constituency.")
    st.write("(d) Photograph: A recent good quality passport-size unsigned colour photograph (4.5cm X 3.5cm) with a white background should be pasted in the space provided. Eyes must be open and both edges of the face must be clearly visible.")
    st.write("(e) Elector's Photo Identity Card (EPIC): EPIC will be delivered at the given postal address after enrolment, free of cost through speed post under proper acknowledgment.")
    st.write("")
    st.write("2. Item (1) *(Name): The exact name and spelling should be furnished in both the official language of the State and English. If filled in only one language, the system will transliterate automatically in the other language, which may lead to spelling mistakes.")
    st.write("3. Item (2a) & (2b) (Name and Surname of Relative): In the case of a married female applicant, the name of the husband may preferably be mentioned. (Strike off the inapplicable options in the column).")
    st.write("4. Item (5) Aadhaar Details: Aadhaar Number should be furnished for the purpose of authentication of entries. If the applicant does not have an Aadhaar number, the same may be mentioned in the box at item 5 (b).")
    st.write("5. Item (6) (Gender):")
    st.write("(a) Gender in the appropriate box provided for 'Male'/'Female'/'Third Gender' should clearly be tick marked.")
    st.write("(b) Applicants belonging to the Third Gender may indicate their sex as 'Male' or as 'Female' or as 'Third Gender'.")
    st.write("6. Item 7(a)(b) (Date of Birth):")
    st.write("(a) A self-attested copy of one of the documents mentioned in the form can be attached as age proof. Submission of a document mentioned in the form will ensure speedy registration and delivery of services.")
    st.write("(b) If none of the documents mentioned in the form is available, the applicant should enclose some other document in support of age proof, and the name of the said document should be mentioned in item 7(ii) and item (iv) of the 'DECLARATION' part in Form. In such a case, the applicant will have to appear personally before the Electoral Registration Officer or any other officer designated by him for verification.")
    st.write("7. Item 8 (Present Ordinary Residence):")
    st.write("(a) Complete postal address with PIN code should be mentioned along with a self-attested copy of any of the mentioned documents in the name of the applicant/parents/spouse as proof of ordinary residence.")
    st.write("(b) Necessary field verification shall be made in cases of Homeless Indian Citizens living in sheds/pavements and sex workers having no documentary proof of ordinary residence, provided they are otherwise eligible for enrollment.")
    st.write("(c) Students, who are eligible for enrollment, can be enrolled either at their parent's place or at the hostel/mess where they are ordinarily residing.")
    st.write("")
    st.write("8. *DECLARATION: All entries in the 'DECLARATION' portion should be filled in correctly and completely.")
    st.write("9. *Verification by Booth Level Officer (BLO): The application form will be verified by the Booth Level Officer to verify the applicant's place of residence.")
    st.write("")
    st.write("10. The application can be submitted directly to the Electoral Registration Officer/Assistant Electoral Registration Officer/Booth Level Officer of the concerned polling station or can be sent by post or can be handed over to the Designated Officer(s) authorized by the Election Commission of India, such as the Post Office, Common Service Centres, etc. The list of Designated Officer(s) is available with the Electoral Registration Officer and on the website of the Chief Electoral Officer of the concerned State/UT.")
    st.write("")
    st.write("11. Acknowledgment: The applicant should mention his/her mobile number and/or email ID in the application form to receive the acknowledgement. The applicants can also track the status of their application through the online portal of the CEO concerned.")
    st.write("")
    st.write("12. Official Website: For details, please see the website of the Chief Electoral Officer of the concerned state/UT or visit the National Voters' Service Portal (www.nvsp.in).")
    st.write("")
    st.write("13. *Mandatory Fields")
if __name__ == "__main__":
    app()