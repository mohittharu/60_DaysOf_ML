import cv2

img = cv2.imread('05-computer-vision-open/Contour & Shape Detection/circle.png')  # Load an image from file
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert the image to grayscale

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Apply binary thresholding to the grayscale image    
# _ is a placeholder for the return value of cv2.threshold, which is the threshold value used. In this case, we are not using it, so we assign it to _.



# find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the binary image 

# draw the contours on the original image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)  # Draw all contours on the original image in green color with thickness of 2 pixels

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # Approximate the contour to a polygon

    if len(approx) == 3:
        shape_name = "Triangle"

    if len(approx) == 4:
            shape_name = "Rectangle"

    if len(approx) == 5:
            shape_name = "Pentagon"

    else:
            shape_name = "Circle"

    cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)  # Draw the approximated polygon on the original image in red color with thickness of 5 pixels   
    x = approx.ravel()[0]  # Get the x-coordinate of the first vertex of the approximated polygon
    y = approx.ravel()[1]  # Get the y-coordinate of the first vertex of the approximated polygon
    cv2.putText(img, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)  # Put the name of the shape on the




cv2.imshow('Contours', img)
cv2.waitKey(0)  # Wait indefinitely for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows 


# to download the haarfile" https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_smile.xml"