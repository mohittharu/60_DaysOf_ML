import cv2

image = cv2.imread('C:\\Users\\acer\\OneDrive\\Desktop\\60_DaysOf_ML\\05-computer-vision-open\\Filtering&Bluring\\twilight-full-moon-from-a-distance-wallpaper-2560x1080_14.jpg')  # Read the image from file

blurred_image = cv2.GaussianBlur(image, (15, 15), 3)  # Apply Gaussian blur to the image

cv2.imshow('Original Image', image)  # Display the original image in a window
cv2.imshow('Blurred Image', blurred_image)  # Display the blurred image in a window     

cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows