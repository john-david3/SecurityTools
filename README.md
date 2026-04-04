# Security Tools Repository
This repository contains a series of tools that can be used to exploit common vulnerabilities.
**Disclaimer: These tools are for educational purposes only and authorised security testing only. Do not use these tools without explicit permission
As of right now, here are the tools available:

## Password Attacks
- Hybrid Password Attack Tool `password-attacks/hybrid-attack/password_cracker.py`
    - Combines dictionary-based attacks (Top 10 million passwords) with brute-force fallback.
    - The file containing these passwords can be found here: [Top 10million passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/Pwdb_top-10000000.txt)

## Privilege Escalation
- Windows Privilege Escalation Script `privilege-escalation/windows/priv_esc.ps1`
    - Example of how you could use a script to escalate privilege on a windows machine via powershell
    - the `cmd.exe` argument can be changed to any file you wish to run as administrator (opening the command prompt directly may not be very subtle)
    - Credits: John Hammond
