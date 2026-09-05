import cv2 

image = cv2.imread("mohit.png")
# width, height 

if image is None:
    print("Image not found")

else:
    print("Image loaded successfully.")

    cropped_image = image[50:200, 100:300]  # Cropping the image

    cv2.imshow("Original Image", image)

    cv2.imshow("Cropped Image", cropped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()