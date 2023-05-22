# OpenCV Project
A project where Raspberry pi 4 model B has one DHT11 sensor measuring temperature and Humidity. In a code, there is one button what starts the code when pressed plus one LED what has red color.

# Image Acquisition:
Set up your Raspberry Pi with a camera module or an external camera to capture images or video frames of the lock. 
Make sure you have a clear view of the lock and that the images are of sufficient quality for processing.

# Preprocessing:
Preprocess the acquired images to enhance their quality and make subsequent processing steps more effective. 
Common preprocessing techniques include resizing, grayscale conversion, noise reduction, and image enhancement (such as contrast adjustment).

# Object Detection:
Implement object detection techniques to identify the lock and its components (such as the gear or keyhole) in the acquired images. 
OpenCV provides various methods for object detection, including Haar cascades, HOG (Histogram of Oriented Gradients), and deep learning-based approaches like YOLO (You Only Look Once).

# Feature Extraction:
Once the lock or its components are detected, extract relevant features from the image to determine the state of the lock. 
For example, you can extract features from the gear to determine its position or rotation.

# Decision-making and Control:
Analyze the extracted features and make decisions based on the desired lock behavior. 
For instance, if the gear is in the correct position or rotated to a certain angle, you can trigger the motor to open the lock. Define the logic and control mechanisms based on the specific requirements of your lock prototype.

# Integration with Raspberry Pi:
Integrate the image processing code with the Raspberry Pi and control the motor based on the decisions made in the previous step. 
Utilize the appropriate GPIO (General Purpose Input/Output) pins of the Raspberry Pi to interface with the motor and control its movement.


# Libraries
pip install psutil
import psutil
import time

while True:

    temperature = psutil.sensors_temperatures()['cpu-thermal'][0].current
    
    print("CPU Temperature:", temperature)
    
    # Perform other tasks or logic based on the temperature reading

    time.sleep(5)  # Delay for 5 seconds before the next temperature measurement
