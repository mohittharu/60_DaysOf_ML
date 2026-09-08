'''
1- cv2.bitwise_and() - Performs a bitwise AND operation on two images. It takes two images as input and returns an image where each pixel is the result of the AND operation between the corresponding pixels of the input images.
2- cv2.bitwise_or() - Performs a bitwise OR operation on two images. It takes two images as input and returns an image where each pixel is the result of the OR operation between the corresponding pixels of the input images.
3- cv2.bitwise_xor() - Performs a bitwise XOR operation on two images. It takes two images as input and returns an image where each pixel is the result of the XOR operation between the corresponding pixels of the input images.
4- cv2.bitwise_not() - Performs a bitwise NOT operation on an image. It takes a single image as input and returns an image where each pixel is the result of the NOT operation on the corresponding pixel of the input image.
'''

import cv2
import numpy as np

img1 = np.zeros((300, 300), dtype=np.uint8)  # Create a black image of size 300x300
img2 = np.zeros((300, 300), dtype=np.uint8)  # Create another black image of size 300x300

cv2.circle(img1, (150, 150), 100, 255, -1)  # Draw a white circle on img1
cv2.rectangle(img2, (100, 100), (200, 200), 255, -1)  # Draw a white rectangle on img2

and_result = cv2.bitwise_and(img1, img2)  # Perform bitwise AND operation   
or_result = cv2.bitwise_or(img1, img2)   # Perform bitwise OR operation
xor_result = cv2.bitwise_xor(img1, img2)  # Perform bitwise XOR operation
not_result = cv2.bitwise_not(img1)  # Perform bitwise NOT operation on img1 


cv2.imshow('Image 1', img1)  # Display the first image in a window
cv2.imshow('Image 2', img2)  # Display the second image in a window
cv2.imshow('Bitwise AND', and_result)  # Display the result of bitwise AND operation in a window
cv2.imshow('Bitwise OR', or_result)  # Display the result of bitwise OR operation in a window
cv2.imshow('Bitwise XOR', xor_result)  # Display the result of bitwise XOR operation in a window
cv2.imshow('Bitwise NOT', not_result)  # Display the result of bitwise NOT operation in a window
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows 