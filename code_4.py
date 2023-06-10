# well i wanted that after user clicks on next , on another page laptop or device camera's open and they record the face and then matches with the photo which was uploaded in the previous page and then show appropriate result


import streamlit as st
import cv2
import numpy as np
from PIL import Image


# Streamlit app code
def main():
    st.title("Image Upload and Face Detection")

    # Image upload
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Checkbox and next page button
        if st.checkbox("Enable Face Detection"):
            if st.button("Next"):
                # Call face detection function and navigate to the next page
                detect_faces(image)


# Function to detect faces in the uploaded image
def detect_faces(image):
    # Perform face detection using OpenCV or other face detection libraries
    # Example code:
    img_array = np.array(image)
    gray_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    # Perform face detection operations...

    # Open device camera for face recording
    cap = cv2.VideoCapture(0)
    st.title("Face Recording")
    st.write("Please look into the camera and record your face.")
    recording = True

    # Face matching with uploaded photo
    while recording:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the recorded face
        st.image(frame, caption="Recorded Face", use_column_width=True)

        # Perform face matching with the uploaded photo
        # Example code:
        if match_faces(frame, image):
            st.success("Face matched with the uploaded photo.")
        else:
            st.error("Face does not match with the uploaded photo.")

        # Stop recording and release camera
        if st.button("Stop Recording"):
            recording = False
            cap.release()


# Function to match face with the uploaded photo
def match_faces(frame, uploaded_image):
    # Perform face matching using appropriate libraries or techniques
    # Example code:
    uploaded_array = np.array(uploaded_image)
    uploaded_gray = cv2.cvtColor(uploaded_array, cv2.COLOR_RGB2GRAY)
    # Perform face matching operations...


if __name__ == "__main__":
    main()
