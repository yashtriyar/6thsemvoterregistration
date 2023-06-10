#new better code of code_4

import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Streamlit app code
def main():
    st.title("Image Upload and Face Detection")
    
    # Image upload
    uploaded_image = st.file_uploader("Upload an image", type=['jpg', 'jpeg', 'png'])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Checkbox and next page button
        if st.checkbox("Enable Face Detection"):
            if st.button("Next"):
                # Call face detection function and navigate to the next page
                detect_and_match_faces(image)
    
# Function to detect faces in the uploaded image and match with recorded face
def detect_and_match_faces(uploaded_image):
    # Convert the uploaded image to grayscale
    uploaded_array = np.array(uploaded_image)
    uploaded_gray = cv2.cvtColor(uploaded_array, cv2.COLOR_RGB2GRAY)
    
    # Open device camera for face recording
    cap = cv2.VideoCapture(0)
    st.title("Face Recording")
    st.write("Please look into the camera and record your face.")
    recording = True
    
    # Face detection and matching
    while recording:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detect faces in the frame
        detected_image = detect_faces(frame)
        
        # Display the detected faces
        st.image(detected_image, caption="Detected Faces", use_column_width=True)
        
        # Perform face matching with the uploaded photo
        if match_faces(frame, uploaded_gray):
            st.success("Face matched with the uploaded photo.")
        else:
            st.error("Face does not match with the uploaded photo.")
        
        # Stop recording and release camera
        if st.button("Stop Recording"):
            recording = False
            cap.release()

# Function to detect faces in the image
def detect_faces(image):
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Load the face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)

    # Draw a bounding box around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return image

# Function to match face with the uploaded photo
def match_faces(frame, uploaded_gray):
    # Convert the frame to grayscale
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # Resize the uploaded grayscale image to match the frame size
    uploaded_gray_resized = cv2.resize(uploaded_gray, (grayscale_frame.shape[1], grayscale_frame.shape[0]))
    
    # Calculate the distance between the faces
    distance = cv2.norm(grayscale_frame, uploaded_gray_resized, cv2.NORM_L2)

    # If the distance is less than a threshold, then the faces match
    if distance < 100:
        return True
    else:
        return False

if __name__ == "__main__":
    main()

