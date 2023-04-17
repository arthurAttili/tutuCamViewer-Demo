from configs import *
import cv2

rtsp_url = f"rtsp://{login}:{password}@{ip_camera_1}:554/stream1"
cap = cv2.VideoCapture(rtsp_url)

# Get the video stream's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #// 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #// 2
fps = cap.get(cv2.CAP_PROP_FPS)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        # Display the frame
        cv2.imshow(name_camera_1, frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()