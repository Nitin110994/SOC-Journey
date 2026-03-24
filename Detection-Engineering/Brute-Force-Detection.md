# Detection Use Case: Brute Force Login Detection

## Objective
The goal is to detect brute force attacks by identifying multiple failed login attempts within a short time.

---

## Log Source
- Windows Security Event Logs
- Event ID: 4625 (Failed Login)

---

## Detection Logic
Trigger an alert when more than 5 failed login attempts happen within 2 minutes.

---

## Detection Rule
IF failed_login_attempts > 5 within 2 minutes  
THEN trigger alert "Possible Brute Force Attack"

---

## Example Query (KQL)

SecurityEvent
| where EventID == 4625
| summarize FailedAttempts = count() by Account, IPAddress, bin(TimeGenerated, 2m)
| where FailedAttempts > 5

---

## Alert Details
- Alert Name: Brute Force Attempt Detected
- Severity: Medium
- Attack Type: Credential Access

---

## SOC Analyst Actions
- Check which account is affected
- Verify the source IP address
- Look for successful login after failures
- Block or investigate suspicious IP

---

## False Positives
- User entering wrong password multiple times
- Misconfigured applications

---

## False Negatives
- Slow brute force attacks
- Attacks from multiple IP addresses

---
