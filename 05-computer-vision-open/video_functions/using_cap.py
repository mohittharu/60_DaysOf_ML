import cv2

cap = cv2.VideoCapture(0)   #start the webcam

while True:
    ret, frame = cap.read()   #read a frame from the webcam
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow('webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):    #wait for 1 ms and check if 'q' key is pressed
        print("Quitting...")
        break


cap.release()
cv2.destroyAllWindows()
