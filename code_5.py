#bard with new github library code. lets see if this works



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
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load the face cascade
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)

    # Draw a bounding box around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image


# Function to match face with the uploaded photo
def match_faces(frame, uploaded_image):
    # Convert the frame to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert the uploaded image to grayscale
    uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_RGB2GRAY)

    # Calculate the distance between the faces
    distance = cv2.norm(grayscale_frame, uploaded_gray, cv2.NORM_L2)

    # If the distance is less than a threshold, then the faces match
    if distance < 100:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
