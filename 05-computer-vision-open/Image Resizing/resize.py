import cv2

image = cv2.imread("mohit.png")


if image is None:
    print("Image not found or unable to load.")

else:
    print("Image loaded successfully.")

    resized_image = cv2.resize(image, (300, 300))

    cv2.imshow("Original Image", image )

    cv2.imshow("Resized Image", resized_image)

    cv2.imshow("resized_output", resized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()