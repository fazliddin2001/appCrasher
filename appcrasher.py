import os, time

def crashApp(name, times=10, wait=1):
    while(times > 0):
        os.system(f"TASKKILL /F /IM {name}.exe")
        time.sleep(wait)
        os.system(f"start {name}")
        times -= 1
