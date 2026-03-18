# 🔍 Network Scanning & Port Investigation Lab

## 📌 Objective

To perform network reconnaissance, service enumeration, and host-based investigation using Nmap and Windows tools, and analyze network behavior such as CLOSE_WAIT connections.

---

## 🖥️ Lab Setup

* **Attacker Machine:** Kali Linux (192.168.223.4)
* **Target Machine:** Windows (192.168.223.5)
* **Environment:** VirtualBox

---

## 🔎 Step 1: Initial Scan

### Command:

nmap -sV 192.168.223.5

### Findings:

* 135/tcp → MSRPC
* 139/tcp → NetBIOS
* 445/tcp → SMB

### Analysis:

Identified a Windows machine with SMB exposed, which is a common entry point for attackers.

---

## 🔍 Step 2: SMB Enumeration Attempt

### Commands:

nmap --script smb-enum-shares -p 445 192.168.223.5
smbclient -L //192.168.223.5/ -N

### Findings:

* Access denied (NT_STATUS_ACCESS_DENIED)

### Analysis:

Anonymous SMB access is disabled, indicating basic system hardening.

---

## 🧪 Step 3: Vulnerability Scan

### Commands:

nmap --script smb-vuln* -p 445 192.168.223.5
nmap --script vuln -p 445 192.168.223.5

### Findings:

* No confirmed vulnerabilities detected
* Some scripts failed due to restricted access

### Analysis:

Unauthenticated scans provide limited visibility; further analysis required.

---

## 🔐 Step 4: SMB Protocol Analysis

### Command:

nmap --script smb-protocols -p 445 192.168.223.5

### Findings:

* SMBv2 and SMBv3 enabled
* SMBv1 disabled

### Analysis:

System is protected against legacy SMB exploits such as EternalBlue.

---

## 🌐 Step 5: Full Port Scan

### Command:

nmap -p- -sV 192.168.223.5

### Findings:

* Standard Windows ports: 135, 139, 445
* Dynamic RPC ports: 49664–49673
* Unknown port: 5040

---

## 🔍 Step 6: Port 5040 Investigation

### Commands (Windows):

netstat -ano | findstr :5040
tasklist /FI "PID eq 1768"
tasklist /svc /FI "PID eq 1768"

### Findings:

* Port 5040 mapped to svchost.exe
* Service identified as CDPSvc (Connected Devices Platform Service)

### Analysis:

Port 5040 is associated with a legitimate Windows service.

---

## 🌐 Step 7: Network Connection Analysis

### Observation:

* Multiple CLOSE_WAIT connections from 192.168.223.4

### Analysis:

* Source IP corresponds to Kali Linux scanning machine
* CLOSE_WAIT state indicates connections not fully closed
* Behavior is consistent with active scanning and probing

---

## 🎯 Key Learnings

* Identifying open ports and services using Nmap
* Understanding SMB exposure and security posture
* Importance of full port scanning beyond default range
* Mapping ports to processes and services
* Interpreting TCP connection states (CLOSE_WAIT)
* Differentiating between normal scanning activity and suspicious behavior

---

## ✅ Conclusion

This lab demonstrated a complete workflow from network scanning to host-based investigation, highlighting how to analyze exposed services and validate system behavior through process and connection analysis.

---
