# Day7-9: Windows Detection & Threat Hunting Notes

---

# 1. Windows Event Logs Basics

## What is a Log?

A log is a record of an event that happened on a system.

Examples:
- User login
- Process start
- Network connection
- File creation
- Registry modification

Logs help SOC analysts understand what happened on a system.

---

# 2. Windows Log Categories

## Application Logs
- Information about applications (Notepad, Chrome, etc.)

## System Logs
- System issues
- Driver errors
- Updates

## Security Logs
- Login and logout activity
- Failed login attempts
- Privilege assignments
- Security-related actions

## Setup Logs
- Windows installation and update events

---

# 3. Important Windows Security Event IDs

- **4624** – Successful login  
- **4625** – Failed login  
- **4672** – Special privileges assigned  
- **4688** – Process created  

These are critical for SOC investigations.

---![successful logon](https://github.com/user-attachments/assets/e21ccdae-b343-46d2-9d69-5910e5e74864)
### Event ID 4624 – Successful Logon

Indicates a successful login attempt.

SOC Use:
- Confirm user authentication
- Detect suspicious login times
- Identify remote access

![failed logon](https://github.com/user-attachments/assets/3bdbfd6f-a634-4733-afda-ab793f21e7f6)
### Event ID 4625 – Failed Logon

Indicates a failed login attempt.

SOC Use:
- Detect brute-force attempts
- Monitor password spraying
- Investigate repeated failures

# 4. Accessing Windows Logs

Logs are stored in: .evtx


Access methods:
- Event Viewer (`eventvwr`)
- PowerShell
- Command line tools

---

# 5. PowerShell Log Investigation

## Get-WinEvent

Used to retrieve events from:
- Event logs
- Event trace files
- Local or remote systems

### Useful Parameters

- `-ListLog`
- `-ListProvider`
- `Where-Object`
- `-FilterHashtable`

---

# 6. XPath Queries

Windows event logs use XML format.

XPath is used to filter events.

Queries often start with: * or event


Used for advanced filtering in investigations.

---

# 7. Sysmon (System Monitor)

Sysmon enhances Windows logging.

It provides visibility into:
- Process creation
- Network connections
- File creation
- Registry changes
- DLL loading
- Process injection

Important:
- Not enabled by default
- Uses XML configuration
- Found under Applications and Services Logs

---

# 8. Important Sysmon Event IDs

- **Event ID 1** – Process creation  
- **Event ID 3** – Network connection  
- **Event ID 7** – Image (DLL) loaded  
- **Event ID 8** – CreateRemoteThread (process injection)  
- **Event ID 11** – File created  
- **Event ID 12, 13, 14** – Registry changes  
- **Event ID 22** – DNS query  

---

# 9. Suspicious Parent-Child Processes

Monitor abnormal process relationships.

Examples:
- Word → PowerShell  
- Excel → cmd.exe  
- Browser → unknown executable  

These may indicate exploitation or malware.

---

# 10. Hunting Metasploit

Metasploit is a penetration testing tool.

Indicators:
- Connections on suspicious ports (4444, 5555)
- Unknown outbound IP connections
- Reverse shell behavior

Unknown IP connections should always be investigated.

---

# 11. Hunting Mimikatz (Credential Dumping)

Mimikatz targets the LSASS process.

Detection approach:
- Monitor abnormal process access to LSASS
- If processes other than legitimate ones access LSASS, investigate
- Look for suspicious process behavior

---

# 12. Malware Hunting Approach

Basic hunting steps:

1. Review logs
2. Identify suspicious ports
3. Detect unknown IP connections
4. Monitor process creation
5. Check registry changes
6. Inspect DNS queries
7. Use packet capturing if necessary

---

# 13. wevtutil (Command Line Tool)

Used to manage Windows event logs.

Common commands:

List logs: wevtutil el

Query events:
wevtutil qe Security /c:10 /rd:true


Options:
- `/rd` – Read newest events first
- `/c` – Limit number of events

---

# 14. SOC Investigation Flow

When investigating:

1. Check authentication logs (4624 / 4625)
2. Check privilege escalation (4672)
3. Check process creation (4688 or Sysmon ID 1)
4. Check network activity (Sysmon ID 3)
5. Check DNS queries (Sysmon ID 22)
6. Check registry changes (12, 13, 14)

Correlating these events helps detect:
- Brute-force attacks
- Credential compromise
- Malware execution
- Lateral movement
- Data exfiltration

---

# Summary

Windows logs + Sysmon provide deep visibility into:

- Authentication activity
- Process execution
- Network communication
- File changes
- Registry modifications
- DNS activity

Threat hunting requires correlating these logs to identify adversary behavior early.




