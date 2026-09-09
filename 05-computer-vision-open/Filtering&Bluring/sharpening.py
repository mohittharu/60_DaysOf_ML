import cv2
import numpy as np


image = cv2.imread('C:\\Users\\acer\\OneDrive\\Desktop\\60_DaysOf_ML\\05-computer-vision-open\\Filtering&Bluring\\twilight-full-moon-from-a-distance-wallpaper-2560x1080_14.jpg')  # Read the image from file

# apply sharpening filter to the image
sharpen_kernel = np.array([[0, -1, 0], 
                           [-1, 5,-1],
                             [0, -1, 0]])  # Define the sharpening kernel

sharpened_image = cv2.filter2D(image, -1, sharpen_kernel)  # Apply the sharpening filter to the image   

cv2.imshow('Original Image', image)  # Display the original image in a window
cv2.imshow('Sharpened Image', sharpened_image)  # Display the sharpened

cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows

