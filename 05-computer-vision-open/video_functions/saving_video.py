import cv2  

camera = cv2.VideoCapture(0)  # Start the webcam

frame_width = int(camera.get(3))  # Get the width of the frame
frame_height = int(camera.get(4))  # Get the height of the frame


# Define the codec and create a VideoWriter object to save the video
codec = cv2.VideoWriter_fourcc(*'XVID')  # Define the codec (XVID)

recorder = cv2.VideoWriter('recorded_video.avi', codec, 20.0, (frame_width, frame_height))  # Create a VideoWriter object

while True:
    success, frame = camera.read()  # Read a frame from the webcam

    if not success:
        print("Failed to grab frame")
        break

    recorder.write(frame)  # Write the frame to the video file

    cv2.imshow('Recording', frame)  # Display the frame in a window 

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for 1 ms and check if 'q' key is pressed
        print("Quitting...")
        break

camera.release()  # Release the webcam
recorder.release()  # Release the VideoWriter object
cv2.destroyAllWindows()  # Close all OpenCV windows
