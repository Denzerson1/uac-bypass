# Windows Defender and UAC Bypass Script

## Introduction
This script is designed to disable Windows Defender and perform a User Account Control (UAC) bypass by manipulating registry settings. It serves as a demonstration of understanding Windows security mechanisms and registry manipulation in the context of security bypass techniques.

Script Components
1. Windows Defender Disablement
The disable_windows_defender() function modifies the registry key associated with Windows Defender to disable its anti-spyware functionality. This manipulation effectively bypasses Windows Defender's protection mechanisms, allowing potentially harmful actions to be executed without detection.

Purpose:
Disabling Windows Defender allows for the execution of unauthorized commands or programs without being blocked by Windows Defender's security measures.
Registry Modification:
Key Path: HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender
Value Name: DisableAntiSpyware
Value Type: REG_DWORD
Value Data: 1 (Enabled)
2. User Account Control (UAC) Bypass
The fodhelper_bypass() function exploits the Fodhelper application to execute a specified command or program with elevated privileges. This bypasses the restrictions imposed by User Account Control (UAC) and allows for the execution of potentially malicious actions without user consent.


Bypassing UAC enables the execution of commands or programs with elevated privileges without triggering user prompts or warnings.
Registry Modification:
Key Path: HKEY_CURRENT_USER\Software\Classes\ms-settings\Shell\Open\command
Value Name: (default)
Value Data: Path to the command or program to be executed with elevated privileges
Usage

Create the Registry Structure
Initiate fdhelper.exe
The following checks are performed in the registry upon start of fodhelper.exe:

1 - HKCU:\Software\Classes\ms-settings\shell\open\command
2 - HKCU:\Software\Classes\ms-settings\shell\open\command\DelegateExecute
3 - HKCU:\Software\Classes\ms-settings\shell\open\command\(default)
Since these registry entries doesn’t exist a user can create this structure in the registry in order to manipulate fodhelper to execute a command with higher privileges bypassing the User Account Contol (UAC).

Remove Registry entries

Note
Use this script responsibly and only on systems you own or have explicit permission to modify.
Modifying system settings and disabling security features can expose your system to various security threats.
