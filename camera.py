import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit(-1)

# Opens camera and starts grayscale
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