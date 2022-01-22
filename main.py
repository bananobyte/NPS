import os
import platform

try:
    from rich.console import Console
except ModuleNotFoundError:
    os.system('pip install rich')
console = Console()
with console.status("[bold green]Loading...") as status:
    try:
        import pyfiglet
        import os
        from colorama import Fore, Style
        from nsp import *
    except ModuleNotFoundError:
        import subprocess

        console.log("[*] INSTALLING colorama, pyfiglet, pywin32, psutil and pymem with pip3")
        subprocess.call('pip3 install colorama pyfiglet pywin32 psutil pymem', shell=True)
        print("[i] Please Restart")
        exit()

    flag = pyfiglet.figlet_format("nsp", "slant")
    system = platform.system()


    def clear():
        if system == "Windows":
            subprocess.call("cls", shell=True)
        else:
            os.system('clear')


    def ini():
        print(Fore.GREEN, flag, Style.RESET_ALL)
        print("         v1.1")
        print("[1] Register new processes")
        print("[2] Show processes and IDS")
        print("[3] Start or close the nsp agent")
        print("[4] Check the Register")
        print("[5] Reset Register")
        print("[X] Exiting")
        print()
        cmd = input("[>] >>>").lower()

        if cmd == "1":
            cwd = os.getcwd()
            pn = input("[>] PROCESS-NAME: ")
            f = open(fr'{cwd}\data\blacklist.txt', 'a')
            f.write(f"{pn}\n")
            f.close()
        elif cmd == "2":
            for proc in psutil.process_iter():
                try:
                    processname = proc.name()
                    processID = proc.pid
                    print(processname, ' ::: ', processID)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            input("press enter")
        elif cmd == "3":
            print("[*] ACTIVATING")
            cwd = os.getcwd()
            f = open('data/activate.sys', 'w+')
            f.write("True")
            f.close()
            exit(fr"COMMAND FOR START: python {cwd}\data\pagent.pyw")

        elif cmd == "4":
            def check(p):
                from rich.console import Console
                console = Console()
                tasks = [f"task {count}/{countl}"]

                with console.status("[bold green]Working on tasks..."):
                    while tasks:
                        task = tasks.pop(0)
                        for proc in psutil.process_iter():
                            processName = proc.name()
                            try:
                                if processName == line:
                                    console.log(f"{task} {processName} FOUND")
                                    return processName
                                else:
                                    pass
                            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                                pass

            countl = 0
            cwd = os.getcwd()
            with open(fr'{cwd}\data\blacklist.txt', 'r') as f:
                for line in f:
                    countl += 1
            lines = []
            with open(fr'{cwd}\data\blacklist.txt') as f:
                lines = f.readlines()
            count = 0
            if system == "Windows":
                subprocess.call("cls", shell=True)
            else:
                os.system('clear')
            for line in lines:
                line = line.rstrip('\n')
                count = count + 1
                e = check(line)
                if e != 0:
                    if e is None:
                        console.log(f"{count}/{countl} {line} NOT FOUND")
                    else:
                        kill_by_win_taskkill(e)
                else:
                    pass
            print(f"{Fore.CYAN}[+]{Style.RESET_ALL} Complete")
            input("press enter")

        elif cmd == "5":
            print("[+] RESENTED")
            open("data/blacklist.txt", "w+").close()
            sleep(0.5)

        elif cmd == "x":
            exit(0)

while True:
    clear()
    ini()
