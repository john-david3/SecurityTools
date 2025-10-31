# Security Tools Repository
This repository contains a series of tools that can be used to exploit common vulnerabilities. These tools are purely for educational purposes and should not be used with malintent
As of right now, here are the tools available:
- Brute Force Password Breaker `pass_break.py`
- Windows Privilege Escalation `PrivilegeEscalation.ps1`

## Brute Force Password Breaker
- Reads from a file containing the top 10 million passwords, if password is not in this file, begin brute forcing
- The file containing these passwords is not attached in this repository but can be found here: [Top 10million passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)

## Windows Privilege Escalation
- Example of how you could use a script to escalate privilege on a windows machine via powershell
- the `cmd.exe` argument can be changed to any file you wish to run as administrator (opening the command prompt directly may not be very subtle)
- Credits: John Hammond
