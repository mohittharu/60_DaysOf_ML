import cv2

# Read the image
image = cv2.imread(
    r"C:\Users\acer\OneDrive\Desktop\60_DaysOf_ML\05-computer-vision-open\Filtering&Bluring\twilight-full-moon-from-a-distance-wallpaper-2560x1080_14.jpg"
)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image. Check the file path.")
else:
    # Apply median blur
    blurred_image = cv2.medianBlur(image, 5)

    # Display original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()