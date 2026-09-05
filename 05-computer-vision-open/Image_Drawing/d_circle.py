import cv2

image = cv2.imread("mohit.png")
if image is None:
    print("Image not found or unable to load.")
else:
    print("Image loaded successfully.")

    # Define the center of the circle
    center = (100, 100)  # Center coordinates (x, y)

    # Define the radius of the circle
    radius = 50

    # Define the color of the circle in BGR format (Blue, Green, Red)
    color = (0, 255, 0)  # Green color

    # Define the thickness of the circle border
    thickness = 2

    # Draw the circle on the image
    image_with_circle = cv2.circle(image.copy(), center, radius, color, thickness)

    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Circle", image_with_circle)

    cv2.waitKey(0)
    cv2.destroyAllWindows()