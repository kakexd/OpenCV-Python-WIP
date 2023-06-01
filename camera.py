import cv2
from tqdm import tqdm
from cascadetraining import CascadeTrain
# tqdm represents a progress bar to show camera finding progression

# making an index to open every single camer from range 0-s_index
# this will search all cameras in this case: one built-in and another is with USB
# None the less, the index finds 2 cameras and following the code:
s_index = 0
e_index = 9

# Creating a progress bar for identifying camera
pbar = tqdm(total=s_index - e_index + 1)

cap = None

# Setting a path to the cascadetraining files

positive_images_dir = 'C:\\Users\\kalle.lehto\\oparicv\\HumidityNtemperature\\pictures\\Positive\\'
negative_images_dir = 'C:\\Users\\kalle.lehto\\oparicv\\HumidityNtemperature\\pictures\\Negative'
cascade_file = 'C:\\Users\\kalle.lehto\\oparicv\\HumidityNtemperature\\xml'

# Create an instance of the CascadeTrain
trainer = CascadeTrain(positive_images_dir, negative_images_dir, cascade_file)

# Train the cascade classifier
trainer.train()


# Finding any camera available to use

for index in range(s_index, e_index + 1):
    # VideoCapture(index) where there is 2 cameras
    cap = cv2.VideoCapture(index)

    if cap.isOpened():

        # Finds the camera
        print(f"camera {index} is opened")
        break

    # Updating a progressbar
    pbar.update(1)

# Closing the progressbar
pbar.close()


# There's no camera available   
if cap is None or not cap.isOpened():
    exit(-1)

# Loading trained detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Camera opens with grayscale what is colored black and white
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Performing facial detection
    faces = face_cascade.detectMultiScale(edges, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Drawing rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    edges = cv2.GaussianBlur(edges, (7, 7), 1.5, 1.5)
    edges = cv2.Canny(edges, 0, 30, 3)
    colored_edges = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    
    cv2.imshow('edges', edges)
    cv2.imshow('colored_edges', colored_edges)
    cv2.imshow('frame', frame)
    if cv2.waitKey(30) >= 0:
        break
    
cap.release()
cv2.destroyAllWindows()