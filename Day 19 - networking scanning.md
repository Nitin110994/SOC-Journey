# Network Scanning & Port Investigation Lab

## Objective

In this lab, I practiced scanning a Windows machine using Nmap, checking open ports, and investigating what services are running. I also looked into network connections like CLOSE_WAIT to understand system behavior.

---

## Lab Setup

* **Attacker Machine:** Kali Linux (192.168.223.4)
* **Target Machine:** Windows (192.168.223.5)
* **Environment:** VirtualBox


<img width="2165" height="549" alt="Blank diagram" src="https://github.com/user-attachments/assets/1f1c6dfc-9a24-4e93-998f-b71ec3fc0ce3" />

---

## Step 1: Initial Scan

### Command:

nmap -sV 192.168.223.5

### Findings:

* 135/tcp → MSRPC
* 139/tcp → NetBIOS
* 445/tcp → SMB

### Analysis:

The system is a Windows machine and SMB is open, which is commonly targeted in attacks.

<img width="1920" height="922" alt="full ports scan" src="https://github.com/user-attachments/assets/c2f842c2-5a83-43a6-99ed-6c2949b31cc5" />


---

## Step 2: SMB Enumeration Attempt

### Commands:

nmap --script smb-enum-shares -p 445 192.168.223.5
smbclient -L //192.168.223.5/ -N

### Findings:

* Access denied (NT_STATUS_ACCESS_DENIED)

### Analysis:

Anonymous SMB access is disabled, indicating basic system hardening.

<img width="1920" height="922" alt="SMB enum scan and os discovery" src="https://github.com/user-attachments/assets/cf6fc157-0892-45e0-bbf2-7e797323affe" />


---

## Step 3: Vulnerability Scan

### Commands:

nmap --script smb-vuln* -p 445 192.168.223.5
nmap --script vuln -p 445 192.168.223.5

### Findings:

* No confirmed vulnerabilities detected
* Some scripts failed due to restricted access

### Analysis:

Unauthenticated scans provide limited visibility; further analysis required.

<img width="1920" height="922" alt="vulnerability scan" src="https://github.com/user-attachments/assets/de3466f9-2121-4a0f-be0f-ff73f4602a90" />


---

## 🔐 Step 4: SMB Protocol Analysis

### Command:

nmap --script smb-protocols -p 445 192.168.223.5

### Findings:

* SMBv2 and SMBv3 enabled
* SMBv1 disabled

### Analysis:

System is protected against legacy SMB exploits such as EternalBlue.

<img width="1920" height="922" alt="vulnerability scan" src="https://github.com/user-attachments/assets/512331db-cb55-4615-b86c-0f135558316b" />


---

## Step 5: Full Port Scan

### Command:

nmap -p- -sV 192.168.223.5

### Findings:

* Standard Windows ports: 135, 139, 445
* Dynamic RPC ports: 49664–49673
* Unknown port: 5040

---

## Step 6: Port 5040 Investigation

### Commands (Windows):

netstat -ano | findstr :5040
tasklist /FI "PID eq 1768"
tasklist /svc /FI "PID eq 1768"

### Findings:

* Port 5040 mapped to svchost.exe
* Service identified as CDPSvc (Connected Devices Platform Service)

### Analysis:

Port 5040 is associated with a legitimate Windows service.

<img width="1280" height="720" alt="port process maping" src="https://github.com/user-attachments/assets/dfa3d1d4-b9dc-4f92-ab05-9f595d28eba8" />


---

## Step 7: Network Connection Analysis

### Observation:

* Multiple CLOSE_WAIT connections from 192.168.223.4

* <img width="1280" height="720" alt="pid" src="https://github.com/user-attachments/assets/4a67a321-3e14-4db9-abac-e06107a209ad" />


### Analysis:

* Source IP corresponds to Kali Linux scanning machine
* CLOSE_WAIT state indicates connections not fully closed
* Behavior is consistent with active scanning and probing

---

## Key Learnings

How to use Nmap for scanning and service detection

How SMB works and why it is important

How to check if a system is hardened

How to scan all ports, not just default ones

How to map a port to a process in Windows

What CLOSE_WAIT means in real scenarios

---

## Conclusion

In this lab, I went from scanning a system to investigating a specific port and understanding network behavior. It helped me understand how attackers see a system and how to analyze it from a SOC perspective.

---
