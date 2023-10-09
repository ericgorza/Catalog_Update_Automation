## CHECKS THE SYSTEMS HEALTH AND RAISES ERRORS IF NEEDED ##

import psutil
import socket
import emails

## Tresholds:

max_cpu_usage = 80
max_disk_space = 20
max_mem_available = 500
chack_local_ip = "127.0.0.1"

# Functions to check the system:

def checkCPU():
    cpu_usage = psutil.cpu_percent(interval=3)
    return cpu_usage > max_cpu_usage

def checkDisk():
    disk_acceptable = 100 - max_disk_space
    disk_space_usage = psutil.disk_usage("/").percent
    return disk_space_usage > disk_acceptable

def checkMemory():
    megabyte = 2**20
    max_memory_acceptable = megabyte * max_mem_available
    mem_available = psutil.virtual_memory().available
    return mem_available < max_memory_acceptable

def checkIP():
    local_host_ip = socket.gethostbyname("localhost")
    return local_host_ip != chack_local_ip

# Function to build and send the email:

def sendAlert(error):
    email_content = {
        "sender":"automation@example.com",
        "receiver":"<username>@example.com",
        "subject":error,
        "body":"Please check the health of your system.",
        "attachment":None
    }
    try:
        message = emails.generate_email(**email_content)
        emails.send_email(message)
    except:
        print("Unable to send the email")

## Calls the functions:

def main():
    error = None
    if checkCPU():
        error = f"Error - CPU usage is over {max_cpu_usage}%"
    elif checkDisk():
        error = f"Error - Available disk space is less than {max_disk_space}%"
    elif checkMemory():
        error = f"Error - Available memory is less than {max_mem_available}MB"
    elif checkIP():
        error = f"Error - localhost cannot be resolved to {chack_local_ip}"

    if error:
        sendAlert(error)
    else:
        print("System healthy.")

if __name__ == "__main__":
    main()