import psutil
import time
from playsound import playsound

def check_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged_status = battery[2]
    #print(f"Battery Level: {percent}")
    if plugged_status and percent == 100:  #battery.power_plugged not working for some reason
        return True
    else:
        return False

def is_plugged():
    battery = psutil.sensors_battery()
    print(battery[2])


def main():
    mp3_file_path = "WhatsApp-Ptt-2023-09-21-at-9.36.34-PM.mp3" #thanks abdul - voice sample
    while True:
        if check_battery():
            print("Battery is fully charged yo!")
            playsound(mp3_file_path)
            break
        else:
            print("Nahhhh not yet.")
        time.sleep(20)  # Check battery status every 20seconds
    
    #is_plugged()
   
if __name__ == "__main__":
    main()
