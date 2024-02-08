import os
import platform
import subprocess
import tkinter as tk
from tkinter import messagebox

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if result.returncode == 0:
            return result.stdout.decode().strip()
        else:
            return result.stderr.decode().strip()
    except Exception as e:
        return str(e)

def get_mac_address():
    if platform.system() == "Windows":
        return run_command("ipconfig /all | findstr /C:'Physical Address'").split()[-1]
    elif platform.system() == "Darwin":
        return run_command("ifconfig en0 | awk '/ether/{print $2}'")
    else:
        return run_command("ifconfig | grep ether | head -n 1 | awk '{print $2}'")

def get_motherboard_serial_number():
    if platform.system() == "Windows":
        return run_command("wmic baseboard get serialnumber").split()[-1]
    elif platform.system() == "Darwin":
        return run_command("system_profiler SPHardwareDataType | awk '/Serial/ {print $4}'").strip()
    else:
        return "Not supported on this platform"

def get_hardware_ids():
    if platform.system() == "Windows":
        return run_command("wmic csproduct get UUID").strip()
    else:
        return "Not supported on this platform"

def get_ip_address():
    if platform.system() == "Windows":
        return run_command("ipconfig | findstr IPv4").split(":")[-1].strip()
    elif platform.system() == "Darwin":
        return run_command("ifconfig | grep 'inet ' | grep -v '127.0.0.1' | awk '{print $2}'")
    else:
        return run_command("hostname -I").strip()

def get_windows_unique_identifier():
    if platform.system() == "Windows":
        return run_command("wmic csproduct get UUID").strip()
    else:
        return "Not supported on this platform"

def get_monitor_info():
    if platform.system() == "Windows":
        return run_command("wmic desktopmonitor get screenwidth,screenheight").strip()
    elif platform.system() == "Darwin":
        return run_command("system_profiler SPDisplaysDataType | grep Resolution").strip()
    else:
        return "Not supported on this platform"

def display_info():
    try:
        mac_address = get_mac_address()
        motherboard_serial = get_motherboard_serial_number()
        hardware_ids = get_hardware_ids()
        ip_address = get_ip_address()
        windows_unique_id = get_windows_unique_identifier()
        monitor_info = get_monitor_info()

        info_text = f"Mac Address: {mac_address}\n" \
                    f"Motherboard Serial Number: {motherboard_serial}\n" \
                    f"Hardware IDs: {hardware_ids}\n" \
                    f"IP Address: {ip_address}\n" \
                    f"Windows Unique Identifier: {windows_unique_id}\n" \
                    f"Monitor Info: {monitor_info}"

        messagebox.showinfo("ayann hwid moooooooooo", info_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("hwid checker ni virnnnnnnn")

button = tk.Button(root, text="pindot paraa makita hwid", command=display_info)
button.pack(padx=10, pady=10)

root.mainloop()
