from cv2 import *
import numpy as np
def main():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cvtColor(frame, COLOR_BGR2GRAY)
        # Display the resulting frame
        # faces = face_cascade.detectMultiScale(frame, 1.1, 4)
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        if waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    destroyAllWindows()

if __name__ == "__main__":
    main()