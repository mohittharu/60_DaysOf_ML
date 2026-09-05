import cv2

image = cv2.imread("mohit.png")
if image is None:
    print("Image not found or unable to load.")
else:
    print("Image loaded successfully.")

    # Define the text to be drawn on the image
    text = "Hello, OpenCV!"

    # Define the position where the text will be placed (bottom-left corner)
    position = (50, 100)  # (x, y)

    # Define the font type
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Define the font scale (size of the text)
    font_scale = 1

    # Define the color of the text in BGR format (Blue, Green, Red)
    color = (255, 0, 0)  # Blue color

    # Define the thickness of the text
    thickness = 2

    # Draw the text on the image
    image_with_text = cv2.putText(image.copy(), text, position, font, font_scale, color, thickness)

    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Text", image_with_text)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
