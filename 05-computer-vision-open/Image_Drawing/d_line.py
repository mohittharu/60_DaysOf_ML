import cv2

image = cv2.imread("mohit.png")
if image is None:
    print("Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    # Define the start and end points of the line
    start_point = (50, 50)  # Starting point (x1, y1)
    end_point = (200, 200)  # Ending point (x2, y2)

    # Define the color of the line in BGR format (Blue, Green, Red)
    color = (0, 255, 0)  # Green color

    # Define the thickness of the line
    thickness = 2

    # Draw the line on the image
    image_with_line = cv2.line(image.copy(), start_point, end_point, color, thickness)

    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Line", image_with_line)

    cv2.waitKey(0)
    cv2.destroyAllWindows()