import cv2 as cv

# Create face detection and load cascade classifier
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

# Open video
video_cap = cv.VideoCapture("vid.mp4") # TODO: 0 means open firs webcam

while True:
    # Get a frame from the webcam
    _, frame = video_cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Run frame detection
    faces = face_cascade.detectMultiScale(gray, 1.13, 7)
    for face in faces:
        # Extract face from frame
        x, y, w, h = face
        # Drow rectangle over video feed
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 100, 0), 2)

    # Show annotated frame
    cv.imshow("Face detection", frame) # TODO: dezactiveaza linia si _
    # Quit loop
    if cv.waitKey(1) == ord("q"):
        break
# End while

# Close video feed
video_cap.relese()
# Close all windows
cv.destroyAllWindows()
