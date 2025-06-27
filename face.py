# import cv2

# img = cv2.imread("jaysankar.jpg")
# if img is None:
#   print("Image not found or path is incorrect.")
# else:
#  cv2.imshow("Img",img)
#  cv2.waitKey(0)
import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('Suman.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Face Detected', img)
cv2.waitKey()
cv2.destroyAllWindows()
