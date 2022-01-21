import subprocess
import os
import psutil
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from rich.console import Console




def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def getProcessInfoByName(processName):
    listOfProcessObjects = []
    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess):
           pass
    return listOfProcessObjects


def getProcessInfoByPid(pid):
    process_pid = psutil.Process(pid)
    print(process_pid)


def get_pid_by_name(process):
    process_name = process
    pid = None
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid = proc.pid
    return pid


def get_name_by_pid(pid):
    process_pid = psutil.Process(pid)
    process_name = process_pid.name()
    return process_name


def get_status_by_pid(pid):
    process_pid = psutil.Process(pid)
    process_name = process_pid.status()
    return process_name


def get_parent_pid(pid):
    process_pid = psutil.Process(pid)
    process_name = process_pid.ppid()
    return process_name


def kill_by_pid(pid):
    process_pid = psutil.Process(pid)
    process_name = process_pid.kill


def kill_by_win_taskkill(processname):
    subprocess.call(f"TASKKILL /F /IM {processname}", shell=True)


def kill_by_win_taskkill_pid(pid):
    subprocess.call(f"TASKKILL /F /PID {pid}", shell=True)
