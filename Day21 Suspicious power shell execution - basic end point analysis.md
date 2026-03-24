# Suspicious PowerShell Execution – Basic Endpoint Analysis

## Scenario

While reviewing an endpoint protection dashboard (RAV Endpoint Protection), I observed multiple alerts related to suspicious PowerShell activity. The alerts were marked as *Suspicious.Argument* and required further analysis.


<img width="1247" height="881" alt="Screenshot 2026-03-23 092523" src="https://github.com/user-attachments/assets/74ea2e9f-d4a1-48ca-9461-dab71f20019d" />


---

## What I Observed

* Tool: RAV Endpoint Protection
* Multiple alerts with same pattern
* Process involved:

  * `powershell.exe`
* Arguments (partial):

  * `-NoProfile`
  * `-ExecutionPolicy` (likely bypass)
* Risk level: Suspicious

### Additional Findings:

* Privacy alert: Camera & Microphone might be at risk
* PUP detected: `Norton.Ask.Search`
* File reference: `devtoolslocal.js`

---

## Why This Looked Suspicious

From my understanding:

* PowerShell is commonly used in attacks (Living-off-the-Land technique)
* `-NoProfile` avoids loading user configs → can hide activity
* Execution policy bypass is often used to run malicious scripts
* Same alert repeated 3 times → could indicate persistence or repeated execution

---

## Analysis


<img width="766" height="421" alt="powershell analysis" src="https://github.com/user-attachments/assets/ff572f72-6abc-4c5e-b3b2-ff7ba4062a18" />



This does not confirm malware directly, but there are strong indicators:

* Possible script execution using PowerShell
* Attempt to bypass system restrictions
* Repeated execution suggests:

  * Scheduled task OR
  * Script retry mechanism

Also, presence of PUP shows the system may not be fully secure and could be exposed to unwanted software.

---

## Possible Hypothesis

A suspicious PowerShell command was executed with execution policy bypass.
This might be part of a malicious script trying to run or maintain persistence on the system.

---

## What I Would Investigate Next

If I had access to the system, I would:

* Check **Windows Event Logs**

  * Event ID 4688 (Process Creation)
  * Event ID 4104 (PowerShell logs)

* Identify:

  * Full PowerShell command
  * Parent process (who launched it)

* Look for persistence:

  * Scheduled tasks
  * Registry Run keys
  * Startup programs

* Check network activity:

  * Any suspicious outbound connections

---

## Basic Remediation Steps

* Stop suspicious PowerShell processes
* Remove any unknown scripts or tasks
* Run full antivirus scan
* Remove PUP (Norton Ask Search)
* Reset browser settings if needed

---

## MITRE ATT&CK Mapping

* T1059.001 – PowerShell
* T1547 – Persistence (possible)

---

## What I Learned

* Even simple alerts like PowerShell arguments can indicate deeper issues
* Repeated alerts are important and should not be ignored
* Context (like PUP presence) helps in understanding overall system risk

---

## Note

This is a basic analysis based only on a single screenshot.
In a real SOC environment, deeper investigation with logs and tools would be required.

---
