import streamlit as st
from datetime import datetime
from PIL import Image

# # Set up the form
# title: Student Information Form
def student_form():
    st.markdown(
    "<h1 style='text-align: center;'>Student Information Form</h1>",
    unsafe_allow_html=True
    )
    # Create the form
    with st.form(key='student_form'):
        # Student Information
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        student_id = st.text_input("Student ID")
        email = st.text_input("Email")
        min_date = datetime(1900, 1, 1)
        max_date = datetime.today()

        # Date input with a custom range
        dob = st.date_input("Date of Birth", min_value=min_date, max_value=max_date)

        # Upload Passport Photo
        pass_photo = st.file_uploader("Upload Passport Photo", type=["jpg", "jpeg", "png"])

        # Upload Signature
        signature = st.file_uploader("Upload Signature", type=["jpg", "jpeg", "png"])

        # Submit Button
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        if pass_photo and signature:
            student_data = [first_name,last_name,student_id,str(dob),pass_photo,signature]
            st.success("Form submitted successfully!")
            # Print the details in the terminal
            print("\nForm Submission Details:")
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Student ID: {student_id}")
            print(f"Email: {email}")
            print(f"Date of Birth: {dob}")

            # Since file upload content is binary, we will print just the file names here
            print("Uploaded Files:")
            # resized_image_pass = Image.open(pass_photo).resize((150, 150))
            # st.image(resized_image_pass, caption="Resized Photo", use_column_width=True)
            
            # resized_image_sig = Image.open(signature    ).resize((150, 150))
            # st.image(resized_image_sig, caption="Resized Signature", use_column_width=True)
            print(f"Passport Photo: {pass_photo.name if pass_photo else 'No file uploaded'}")
            print(f"Signature: {signature.name if signature else 'No file uploaded'}")
        else:
            student_data == None
            st.error("Please upload both a passport photo and a signature.")

        return student_data
