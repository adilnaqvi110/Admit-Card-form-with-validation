from form import student_form
from PIL import Image
from torchvision import transforms, models
import streamlit as st #type:ignore
import io
import cv2
import numpy as np

def convert_uploadedfile_to_image(uploaded_file):
    # Read the uploaded file as a byte stream
    image_bytes = uploaded_file.read()
    
    # Convert the byte stream to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    return image

def is_face_photo(image):
    # Ensure the image is in RGB mode
    if image.mode != "RGB":
        image = image.convert("RGB")
    # Convert the PIL image to a NumPy array
    image_np = np.array(image)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    # Load Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Return True if at least one face is detected, otherwise False
    return len(faces) > 0

def main():
    #initialize student form
    student_data = student_form()
    if student_data:
        face = convert_uploadedfile_to_image(student_data[4])
        sig = convert_uploadedfile_to_image(student_data[5])
        if is_face_photo(face):
            print("1st Photo is Correct (face)")
        if not is_face_photo(sig):
            print("2nd Photo is Correct (sig)")

        if (is_face_photo(face)==False) and (is_face_photo(sig)==True):
            face,sig = sig,face
            student_data[4],student_data[5] = student_data[5],student_data[4]
            print("swapped")

if __name__ == "__main__":
    main()
