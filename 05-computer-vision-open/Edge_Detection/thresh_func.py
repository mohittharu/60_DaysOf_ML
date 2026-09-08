import cv2

img = cv2.imread('05-computer-vision-open/Filtering&Bluring/twilight-full-moon-from-a-distance-wallpaper-2560x1080_14.jpg', cv2.IMREAD_GRAYSCALE)

ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # Apply thresholding to the image


cv2.imshow('Original Image', img)  # Display the original image in a window
cv2.imshow('Thresholded Image', thresh_img)  # Display the thresholded image in a window
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows 

