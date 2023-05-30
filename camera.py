import cv2
# making an index to open every single camer from range 0-9
# this will search all cameras in this case: one built-in and another is with USB
# None the less, the index finds 2 cameras and following the code:

for index in range(10):

    # VideoCapture(index) where there is 2 cameras
    cap = cv2.VideoCapture(index)

    if cap.isOpened():

        # Finds the camera
        print(f"camera is opened")
        break

# There's no camera    
if not cap.isOpened():
    exit(-1)

# Here we are using the second camera and cap = cv2.VideoCapture(index) points that 0 = built-in and 1 = USB connected
cap = (cv2.VideoCapture(1) or cv2.VideoCapture(0))

# Camera opens with grayscale what is colored black and white
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(edges, (7, 7), 1.5, 1.5)
    edges = cv2.Canny(edges, 0, 30, 3)
    
    cv2.imshow('edges', edges)
    
    if cv2.waitKey(30) >= 0:
        break

cap.release()
cv2.destroyAllWindows()