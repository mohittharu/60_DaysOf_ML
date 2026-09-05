import cv2

image = cv2.imread("mohit.png")

if image is None:
    print("Image not found or unable to load.") 

else:
    print("Image loaded successfully.")

    flipped_image = cv2.flip(image, 1)  # Flipping the image horizontally

    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Image", flipped_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()