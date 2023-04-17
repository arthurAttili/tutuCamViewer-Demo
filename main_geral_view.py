from configs import *
import cv2

# List with camera informations
cameras_info = [
    {"ip": ip_camera_1, "name":name_camera_1, "login": login, "password": password},
    {"ip": ip_camera_2, "name":name_camera_2, "login": login, "password": password},
    {"ip": ip_camera_3, "name":name_camera_3, "login": login, "password": password},
    {"ip": ip_camera_4, "name":name_camera_4, "login": login, "password": password},
    {"ip": ip_camera_5, "name":name_camera_5, "login": login, "password": password},
]

# Inicialize VideoCapture for each camera
caps = []
for camera_info in cameras_info:
    rtsp_url = f"rtsp://{camera_info['login']}:{camera_info['password']}@{camera_info['ip']}:554/stream1"
    cap = cv2.VideoCapture(rtsp_url)

    # Check if the camera stream is accessible
    if not cap.isOpened():
        print(f"Error: Unable to access the camera {camera_info['name']}. Check if the camera is turned on and the IP is correct.")
        break
    else:
        caps.append(cap)


# Define the camera width and height
new_width_1, new_height_1 = 640, 480
new_width_2, new_height_2 = 640, 480
new_width_3, new_height_3 = 640, 640

while True:
    # List to place the frames for each window
    frames_1 = []
    frames_2 = []
    frames_3 = []

    for i, cap in enumerate(caps):
        ret, frame = cap.read()

        if ret:
            if i < 2:
                # Resize the frame
                resized_frame_1 = cv2.resize(frame, (new_width_1, new_height_1))
                frames_1.append(resized_frame_1)
            if i > 1 and i < 4:
                # Resize the frame
                resized_frame_2 = cv2.resize(frame, (new_width_2, new_height_2))
                frames_2.append(resized_frame_2)
            if i == 4:
                resized_frame_3 = cv2.resize(frame, (new_width_3, new_height_3))
                frames_3.append(resized_frame_3)

    # If every frames are valid, concat them horizontaly on a single window
    if len(frames_1) == 2 and len(frames_2) == 2 and len(frames_3) == 1:
        window_1_frame = cv2.hconcat(frames_1)
        window_2_frame = cv2.hconcat(frames_2)
        window_3_frame = cv2.hconcat(frames_3)
        cv2.imshow(window_name_1, window_1_frame)
        cv2.imshow(window_name_2, window_2_frame)
        cv2.imshow(window_name_3, window_3_frame)
    else:
        break

    # Pause the recording if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the objects and close all the windows
for cap in caps:
    cap.release()

cv2.destroyAllWindows()