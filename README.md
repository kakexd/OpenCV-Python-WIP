# Roadmap 1.0

# Project tools
- OpenCV libary
- CascadeTraining model
- Annonation tools
- https://www.robots.ox.ac.uk/~vgg/software/via/


# OpenCV Project
A project where Raspberry pi 4 model B has one DHT11 sensor measuring temperature and Humidity. In a code, there is one button what starts the code when pressed plus one LED what has red color.

# Image Acquisition: DONE
Set up your Raspberry Pi with a camera module or an external camera to capture images or video frames of the lock. 
Make sure you have a clear view of the lock and that the images are of sufficient quality for processing.

# Preprocessing: W.I.P
Preprocess the acquired images to enhance their quality and make subsequent processing steps more effective. 
Common preprocessing techniques include resizing, grayscale conversion, noise reduction, and image enhancement (such as contrast adjustment).

# Object Detection: W.I.P
Implement object detection techniques to identify the lock and its components (such as the gear or keyhole) in the acquired images. 
OpenCV provides various methods for object detection, including Haar cascades, HOG (Histogram of Oriented Gradients), and deep learning-based approaches like YOLO (You Only Look Once).

# Feature Extraction: W.I.P
Once the lock or its components are detected, extract relevant features from the image to determine the state of the lock. 
For example, you can extract features from the gear to determine its position or rotation.

# Decision-making and Control: W.I.P
Analyze the extracted features and make decisions based on the desired lock behavior. 
For instance, if the gear is in the correct position or rotated to a certain angle, you can trigger the motor to open the lock. Define the logic and control mechanisms based on the specific requirements of your lock prototype.

# Integration with Raspberry Pi: W.I.P comes with migration
Integrate the image processing code with the Raspberry Pi and control the motor based on the decisions made in the previous step. 
Utilize the appropriate GPIO (General Purpose Input/Output) pins of the Raspberry Pi to interface with the motor and control its movement.

# Roadmap 1.1

# Libraries: DONE
pip install psutil

import psutil

import time
self made cascadeTrain model

- this is under A True statement.

    temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current
    
    print("CPU Temperature:", temperature)

    time.sleep(5)  # Delay for 5 seconds before the next temperature measurement
import cv2
import rqdm proggres bar :D

# Annotations files: W.I.P
    While using git.bash, go to the directory where pictures are located with $ ~/file/project/pictures
    
    Next, we want to run the following .exe file to make Positive file from taken pictures.
    Same goes with Negative pictures.
    
    $ /c/Users/name_of_user/file/mainproject/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/
    

Making a set of annotation files for cascade to be trained from. C:/path/user/opencv/pictures/positive/*
from Cascade training, needs to be correct path. So far it gives an error that the file does not exist in the directed path.
\\ work work work

# Roadmap 2.0: W.I.P

# Face detection
Face Detection: Use a face detection algorithm to locate and extract faces from the live feed. 
OpenCV provides the CascadeClassifier class, which can be used with pre-trained Haar cascades or other cascade files for face detection.

# Face recognition: W.I.P
Face Recognition: Train a face recognition model on a dataset of known faces. 
This typically involves collecting images of individuals you want to recognize and extracting facial features from those images. 
OpenCV offers methods such as Local Binary Patterns Histograms (LBPH) and Eigenfaces for face recognition. Alternatively, you can use deep learning-based approaches like OpenCV DNN module with pre-trained models like OpenFace, FaceNet, or VGGFace.

# Matching and recognition: W.I.P
Matching and Recognition: After detecting a face in the live feed, compare it with the known faces in your dataset using the trained face recognition model. 
Compute the similarity or distance between the detected face and the known faces and determine if there is a match. 
A threshold can be set to decide when a match is considered successful.

# Result Display: W.I.P
Displaying Results: Once a match is found, you can display the recognized person's name or ID on the video feed or perform any other desired action based on the recognition result.

# Roadmap 2.1: W.I.P
     
    using a CascadeClassifier constructor.
    first we load a cascade model, either pre-trained or training it yourself
    - cascade = cv2.CascadeClassifier('path/to/cascade.xml')
    
# Migration to Linux: "W.I.P"
Could be possible but instead :,D

# W.I.P
