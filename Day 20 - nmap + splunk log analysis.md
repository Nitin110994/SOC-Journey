# Day 20 – Nmap + Splunk Log Analysis Lab

## Objective

In this lab, I performed an Nmap scan on a Windows machine and then imported the scan results into Splunk. The goal was to understand how SOC analysts work with logs and identify open ports and services.

---

## Lab Setup

* Kali Linux (Attacker) – 192.168.223.4
* Windows Machine (Target + Splunk) – 192.168.223.5

---

## Step 1: Nmap Scan

### Command used:

nmap -sV -oN nmap_day20.txt 192.168.223.5

### What I found:

* 135 → MSRPC
* 139 → NetBIOS
* 445 → SMB
* 8000 → Splunk Web
* 8089 → Splunk Management

### My understanding:

The system is running normal Windows services but also Splunk. SMB and Splunk ports can be important from a security point of view.

---

## Step 2: Transferring Log File

* Started a Python HTTP server on Kali
* Opened it in Windows browser
* Downloaded the Nmap output file

---

## Step 3: Upload to Splunk

* Used “Add Data” in Splunk
* Uploaded `nmap_day20.txt`
* Stored it in the main index

---

## Step 4: Basic Search

### Query:

index=main

### Result:

Confirmed that the Nmap scan data is visible in Splunk.

---

## Step 5: Finding Open Ports

### Query:

index=main "open"

### Result:

Ports found:

* 135, 139, 445
* 8000, 8089

---

## Step 6: Extracting Port and Service

### Query:

index=main
| rex max_match=0 field=_raw "(?<entry>\d+/tcp\s+open\s+\S+)"
| mvexpand entry
| rex field=entry "(?<port>\d+)/tcp\s+open\s+(?<service>\S+)"
| eval port=tonumber(port)
| table port service

### My understanding:

This helped convert raw logs into readable format with port and service columns.

---

## Step 7: Adding Risk Level

### Query:

index=main
| rex max_match=0 field=_raw "(?<entry>\d+/tcp\s+open\s+\S+)"
| mvexpand entry
| rex field=entry "(?<port>\d+)/tcp\s+open\s+(?<service>\S+)"
| eval port=tonumber(port)
| eval risk=case(
port==445,"High (SMB)",
port==8089,"High (Splunk Mgmt)",
port==8000,"Medium (Splunk Web)",
port==135 OR port==139,"Medium (RPC)",
true(),"Low"
)
| where isnotnull(port)
| table port service risk

---

## What I Learned

* How to save Nmap scan output as a log file
* How to upload external logs into Splunk
* How to extract fields using rex
* How to handle multi-value fields using mvexpand
* How to analyze ports and assign risk levels

---

## SOC Insight

* Port 445 (SMB) is commonly used in attacks
* Splunk ports (8000, 8089) should not be openly exposed
* Even normal services can become risks if not monitored

---

## Conclusion

This lab helped me understand how scan data can be analyzed inside a SIEM tool. I learned how to extract useful information from raw logs and think about risk from a SOC perspective.

---
