import streamlit as st
import sqlite3
from PIL import Image

# Connect to SQLite database
conn = sqlite3.connect('aadhar.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS aadhar_images
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              image BLOB)''')

# Set image dimensions
img_width = 500
img_height = 500

# Streamlit app code
def main():
    st.title("Aadhar Card Image Upload")
    
    # Image upload
    uploaded_image = st.file_uploader("Upload Aadhar card image", type=['jpg', 'jpeg', 'png'])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Aadhar card image", use_column_width=True)
        
        # Save image to database
        save_image(image)
        st.success("Aadhar card image saved successfully.")

# Function to save image to database
def save_image(image):
    # Resize image if necessary
    resized_image = image.resize((img_width, img_height))
    
    # Convert image to bytes
    img_byte_arr = resized_image.tobytes()
    
    # Insert image into the database
    c.execute("INSERT INTO aadhar_images (image) VALUES (?)", (img_byte_arr,))
    conn.commit()

# Function to retrieve image from database
def retrieve_image():
    # Retrieve the latest image from the database
    c.execute("SELECT image FROM aadhar_images ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    if result is not None:
        img_byte_arr = result[0]
        image = Image.frombytes('RGB', (img_width, img_height), img_byte_arr)
        return image
    else:
        return None

if __name__ == "__main__":
    main()

# Close database connection
conn.close()
