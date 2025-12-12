import time
import subprocess
import os

def get_ram_gb():
    cmd = "wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /Value"
    output = subprocess.check_output(cmd, shell=True).decode()

    data = {}
    for line in output.splitlines():
        if "=" in line:
            key, value = line.split("=")
            data[key.strip()] = int(value.strip())

    total_mb = data["TotalVisibleMemorySize"] / (1024)
    free_mb  = data["FreePhysicalMemory"] / (1024)
    used_mb  = total_mb - free_mb

    return total_mb, used_mb, free_mb

while True:
    os.system("cls")

    # CPU %
    cpu = subprocess.check_output(
        "wmic cpu get loadpercentage | findstr [0-9]",
        shell=True
    ).decode().strip()

    total, used, free = get_ram_gb()

    ("===== THEO DÕI HỆ THỐNG 1` =====")
    print(f"CPU Usage : {cpu}%")
    print(f"RAM Tổng  : {total:.2f} mb")
    print(f"RAM Dùng  : {used:.2f} mb")
    print(f"RAM Trống : {free:.2f} mb")
    print("==========================================")

    time.sleep(1)