import cv2
img = cv2.imread('05-computer-vision-open/Filtering&Bluring/twilight-full-moon-from-a-distance-wallpaper-2560x1080_14.jpg', cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(img, 100, 200)  # Apply Canny edge detection to the image

cv2.imshow('Original Image', img)  # Display the original image in a window
cv2.imshow('Canny Edge Detection', edges)  # Display the edges detected image in a window
cv2.waitKey(0)  # Wait indefinitely for a key press         
cv2.destroyAllWindows()  # Close all OpenCV windows