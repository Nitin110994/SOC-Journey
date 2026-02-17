# Day 12 – Brute-Force Login Investigation

As part of my SOC learning journey, I conducted a mini investigation based on a simulated brute-force login alert.

The objective was to analyze authentication logs and determine whether the activity represented a real security incident.

---

# 1. Alert Summary

Alert Name: Multiple Failed Login Attempts  
Source: Windows Security Logs  
Event IDs Observed:
- 4625 (Failed Login)
- 4624 (Successful Login)

Time Window: Within a short timeframe  
Target Host: User workstation  

---

# 2. Initial Observation

The alert was triggered due to multiple failed login attempts from the same source IP address.

Shortly after the failed attempts, a successful login (Event ID 4624) was observed.

This pattern is commonly associated with brute-force or password spraying attempts.

---

# 3. Investigation Steps

## Step 1 – Review Failed Logins (Event ID 4625)

I checked:
- Number of failed attempts
- Source IP address
- Target username
- Failure reason

Observation:
Multiple failed login attempts occurred within a short period.

---

## Step 2 – Review Successful Login (Event ID 4624)

I verified:
- Was the successful login from the same IP?
- What was the logon type?
- What time did it occur?

Observation:
The successful login occurred immediately after multiple failures and originated from the same source.

This increases suspicion of brute-force success.

---

## Step 3 – Check for Suspicious Post-Login Activity

After successful login, I reviewed:

- Event ID 4688 (Process Creation)
- PowerShell execution
- New account creation
- RDP sessions
- Network connections

Observation:
No suspicious processes, privilege escalation, or lateral movement were detected during the session.

---

# 4. MITRE ATT&CK Mapping

Brute Force Attempts:
- Tactic: Credential Access
- Technique: Brute Force (T1110)

Successful Login:
- Tactic: Initial Access
- Technique: Valid Accounts (T1078)

---

# 5. Risk Assessment

Risk Level: Medium

Reason:
Although the login pattern suggests brute-force behavior, there was no evidence of:

- Privilege escalation
- Persistence mechanisms
- Lateral movement
- Command and Control activity

However, account compromise is still possible.

---

# 6. Actions Taken

- Recommended password reset for the affected account
- Recommended enabling or verifying MFA
- Advised monitoring account activity for 24–48 hours
- Logged the incident for documentation

---

# 7. Final Classification

Classification: True Positive (Brute-force attempt observed)

Impact: Limited  
No confirmed system compromise detected.

---

# 8. Key Learnings

- Multiple 4625 events followed by 4624 is a red flag.
- Correlation is critical in determining compromise.
- Not every brute-force attempt results in full compromise.
- Post-login activity analysis is essential before escalation.

---

# Conclusion

This mini investigation helped me understand how to approach authentication alerts systematically. 

By reviewing login attempts, correlating events, and analyzing post-login behavior, I was able to determine the risk level and recommend appropriate actions.
