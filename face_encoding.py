
import face_recognition
from tkinter.filedialog import askopenfilename
# Load the jpg file into a numpy array
image = face_recognition.load_image_file(askopenfilename())
# Generate the face encodings
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
