import cv2

face_cascade = cv2.CascadeClassifier('05-computer-vision-open\\face & Object Detection\\haarcascade_frontalface_default.xml')  # Load the pre-trained Haar Cascade classifier for face detection

eye_cascade = cv2.CascadeClassifier('05-computer-vision-open\\face & Object Detection\\haarcascade_eye.xml')  # Load the pre-trained Haar Cascade classifier for eye detection

smile_cascade = cv2.CascadeClassifier('05-computer-vision-open\\face & Object Detection\\haarcascade_smile.xml')  # Load the pre-trained Haar Cascade classifier for smile detection

cap = cv2.VideoCapture(0)  # Start video capture from the default camera (usually the webcam)



while True:
    ret, frame = cap.read()  # Read a frame from the video capture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale for processing

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)  # Detect faces in the grayscale frame


    for (x, y, w, h) in faces:  # Iterate over the detected faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle around each detected face
        roi_gray = gray[y:y + h, x:x + w]  # Region of interest for eyes and smile detection in grayscale
        roi_color = frame[y:y + h, x:x + w]  # Region of interest for eyes and smile detection in color
        """
        x = 100
        y = 150
        w = 80
        h = 80
        
        (100, 150) = top left corner of the rectangle
        w = 80 > 180
        h = 80 > 230
        (180, 230) = bottom right corner of the rectangle
        """
        eyes = eye_cascade.detectMultiScale(roi_gray)  # Detect eyes within the face region
        if len(eyes) >= 2:  # Check if at least two eyes are detected
            cv2.putText(frame, "Eyes Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)  # Display text if eyes are detected
        # for (ex, ey, ew, eh) in eyes:  # Iterate over the detected eyes
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)  # Draw a rectangle around each detected eye


        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22)  # Detect smiles within the face region
        if len(smiles) > 0:  # Check if at least one smile is detected
            cv2.putText(frame, "Smile Detected", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)  # Display text if smile is detected
        # for (sx, sy, sw, sh) in smiles:  # Iterate over the detected smiles
        #     cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)  # Draw a rectangle around each detected smile



    cv2.imshow('Webcam Face Detection', frame)  # Display the frame with detected faces in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for the 'q' key to be pressed to exit the loop
        break   
cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows 
