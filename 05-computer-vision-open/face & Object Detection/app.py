import cv2  

face_cascade = cv2.CascadeClassifier('05-computer-vision-open\\face & Object Detection\\haarcascade_frontalface_default.xml')  # Load the pre-trained Haar Cascade classifier for face detection

cap = cv2.VideoCapture(0)  # Start video capture from the default camera (usually the webcam)   

while True:
    ret, frame = cap.read() # Read a frame from the video capture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert the frame to grayscale for processing


    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)  # Detect faces in the grayscale frame

    """
    This is a simple face detection application using OpenCV.
    It captures video from the default camera and detects faces in real-time.
    detectMultiScale()- method is used to detect faces in the grayscale frame.
    1.1 - balance, not tool slow , blind 
    minNeighbors=5 - how many neighbors each candidate rectangle should have to retain it. 
    This parameter will affect the quality of the detected faces. 
    Higher values result in fewer detections but with higher quality.

    """

    for (x,y,w,h) in faces:  # Iterate over the detected faces
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)  # Draw a rectangle around each detected face

    """
    x,y = top left corner of the rectangle
    (x+w,y+h) = bottom right corner of the rectangle
    face = [
    (100, 150,80,80)face1, 
    (200, 250,80,80)face2]
    x- how far from left, 
    y- how far from top,
    w- width of rectangle,
    h- height of rectangle
    """

    cv2.imshow('Webcam Face Detection', frame)  # Display the frame with detected faces in a window

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for the 'q' key to be pressed to exit the loop
        break

cap.release()  # Release the video capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
