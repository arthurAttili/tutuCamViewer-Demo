from configs import *
import cv2

#Choose camera below and write it on single_camera variable
#Cam 1 = "Garage"
#Cam 2 = "Kitchen"
#Cam 3 = "Bedroom"
#Cam 4 = "Garden"
#Cam 5 = "Aquarium"

#Write it here!
camera = "Cam 1"


name_camera = camera_dict[camera]["name"]
ip_camera = camera_dict[camera]["ip"]

rtsp_url = f"rtsp://{login}:{password}@{ip_camera}:554/stream1"
cap = cv2.VideoCapture(rtsp_url)

# Check if the camera stream is accessible
if not cap.isOpened():
    print("Error: Unable to access the camera. Check if the camera is turned on and the RTSP URL is correct.")
else:
    # Get the video stream's width and height
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #// 2
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #// 2
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened():
        ret, frame = cap.read()

        if ret:

            # Display the frame
            cv2.imshow(name_camera, frame)

            # Exit the loop if the 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()