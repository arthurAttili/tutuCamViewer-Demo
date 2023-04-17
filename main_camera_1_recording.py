from configs import *
import cv2
from datetime import datetime
import random

rtsp_url = f"rtsp://{login}:{password}@{ip_camera_1}:554/stream1"
cap = cv2.VideoCapture(rtsp_url)

# Define the video codec and file output name
fourcc = cv2.VideoWriter_fourcc(*'DIVX') #AVI -- 15s = 8.5Mb

# Get the current date as a string in the format 'YYYYMMDD'
current_date = datetime.now().strftime('%Y%m%d')

#Define the file name and the location
random_number = random.randint(1, 1000) 

file_name = f"{current_date}-{name_camera_1} ({random_number}).avi"
output_file = output_folder + file_name

# Get the video stream's width and height
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #// 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #// 2
fps = cap.get(cv2.CAP_PROP_FPS)

# Create the VideoWriter object
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:

        # resize the frame (in case you need to reduce storage)
        #resized_frame = cv2.resize(frame, (width, height))
        #out.write(resized_frame)
        #cv2.imshow(name_camera_1, resized_frame)

        # Save the frame to the output file
        out.write(frame)

        # Display the frame
        cv2.imshow(name_camera_1, frame)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()