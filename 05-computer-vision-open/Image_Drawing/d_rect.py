import cv2

image = cv2.imread("mohit.png")
if image is None:
    print("Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    # Define the top-left and bottom-right corners of the rectangle
    top_left = (50, 50)  # Top-left corner (x1, y1)
    bottom_right = (200, 200)  # Bottom-right corner (x2, y2)

    # Define the color of the rectangle in BGR format (Blue, Green, Red)
    color = (0, 0, 255)  # Red color

    # Define the thickness of the rectangle border
    thickness = 2

    # Draw the rectangle on the image
    image_with_rectangle = cv2.rectangle(image.copy(), top_left, bottom_right, color, thickness)

    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Rectangle", image_with_rectangle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()