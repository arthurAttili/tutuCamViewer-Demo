#Replace the ip with the ip of the camera
#Replace the camera name if you want
#Replace the login and password

login = "YOURLOGIN"
password = "YOURPASSWORD"

#This is where the video is writen
output_folder = "G:\\Cams"

#Change the ip and the name of the cameras
camera_dict = {
    "Cam 1": 
        {
            "ip": "192.168.00.0", 
            "name": "Garage"
        },
    "Cam 2": 
        {
            "ip": "192.168.00.0", 
            "name": "Kitchen"
        },
    "Cam 3": 
        {
            "ip": "192.168.00.0", 
            "name": "Bedroom"
        },
    "Cam 4": 
        {
            "ip": "192.168.00.0", 
            "name": "Garden"
        },
    "Cam 5": 
        {
            "ip": "192.168.00.0", 
            "name": "Aquarium"
        },
}

#Name of the window with cameras view on main_geral scripts. Replace it if you want!
window_name_1 = "Window_Name_1"
window_name_2 = "Window_Name_2"
window_name_3 = "Window_Name_3"


#Not necessary to change
ip_camera_1 = camera_dict["Cam 1"]["ip"]
name_camera_1 = camera_dict["Cam 1"]["name"]

ip_camera_2 = camera_dict["Cam 2"]["ip"]
name_camera_2 = camera_dict["Cam 2"]["name"]

ip_camera_3 = camera_dict["Cam 3"]["ip"]
name_camera_3 = camera_dict["Cam 3"]["name"]

ip_camera_4 = camera_dict["Cam 4"]["ip"]
name_camera_4 = camera_dict["Cam 4"]["name"]

ip_camera_5 = camera_dict["Cam 5"]["ip"]
name_camera_5 = camera_dict["Cam 5"]["name"]