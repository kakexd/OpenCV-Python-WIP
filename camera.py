import cv2
from tqdm import tqdm


# making an index to open every single camer from range 0-9
# this will search all cameras in this case: one built-in and another is with USB
# None the less, the index finds 2 cameras and following the code:


start_index = 0
end_index = 9

# Creating a progress bar for identifying camera
pbar = tqdm(total=start_index - end_index + 1)

cap = None

# Finding any camera available to use

for index in range(start_index, end_index + 1):
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


# There's no camera    
if cap is None or not cap.isOpened():
    exit(-1)

# Camera opens with grayscale what is colored black and white
while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    edges = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(edges, (7, 7), 1.5, 1.5)
    edges = cv2.Canny(edges, 0, 30, 3)
    colored_edges = cv2.applyColorMap(edges, cv2.COLORMAP_JET)
    
    cv2.imshow('edges', edges)
    cv2.imshow('colored_edges', colored_edges)
    if cv2.waitKey(30) >= 0:
        break
    
cap.release()
cv2.destroyAllWindows()