# Day 11 – Alert Triage Methodology

Today I focused on understanding how alert triage works in a real SOC environment.

I realized that triage is not just about looking at an alert and reacting.  
It is about thinking clearly and methodically before escalating.

---

# What is Alert Triage?

Alert triage is the process of reviewing a security alert and deciding:

- Is this real or false?
- How serious is it?
- What should be done next?

The goal is to quickly filter noise from real threats.

---

# My Personal Alert Triage Checklist

This is the checklist I would follow when investigating an alert.

---

## 1. Understand the Alert First

Before jumping to conclusions:

- What exactly triggered the alert?
- What rule or detection logic caused it?
- What time did it happen?
- What is the severity assigned by the system?

I need to understand what I’m looking at before analyzing further.

---

## 2. Identify the Host (Asset Context)

- Which machine is involved?
- Is it a normal user laptop?
- Is it a server?
- Is it a domain controller?

The importance of the asset affects how serious the alert is.

Example:
PowerShell on a Domain Controller = more concerning than on a user laptop.

---

## 3. Identify the User

- Which account was used?
- Is it an admin account?
- Is it a service account?
- Is the activity normal for this user?

Context matters. An IT admin running PowerShell may be normal. A finance user running encoded PowerShell is suspicious.

---

## 4. Validate the Activity

I ask myself:

- Has this happened before?
- Is this normal behavior?
- Is it during business hours?
- Is there historical baseline data?

Not every suspicious-looking event is malicious.

---

## 5. Look for Red Flags

Depending on the alert type, I check:

Authentication Alerts:
- Multiple failed logins?
- Login from unusual country?
- Impossible travel?

Process Alerts:
- Suspicious parent-child process?
- Word → PowerShell?
- Encoded command (-enc)?

Network Alerts:
- Connection to known malicious IP?
- DNS query to suspicious domain?
- Large outbound data transfer?

---

## 6. Correlate Other Logs

One alert alone rarely tells the full story.

I check:

- 4624 / 4625 (login events)
- 4688 (process creation)
- Sysmon Event ID 1 (process)
- Sysmon Event ID 3 (network)
- Account creation logs
- Scheduled task creation

I try to build a timeline.

---

## 7. Classify the Alert

After reviewing evidence, I decide:

- False Positive
- True Positive
- Benign True Positive
- Needs Escalation

I should not escalate everything, but I should not ignore real threats either.

---

## 8. Determine Severity

Severity depends on:

- Asset criticality
- Privilege level involved
- Stage of attack
- Evidence of lateral movement
- Evidence of persistence

Example of high severity:
- Credential dumping
- New admin account
- Internal RDP after suspicious login

Example of low severity:
- Single failed login
- Known vulnerability scanner activity

---

## 9. Decide Next Action

Based on findings:

- Close the alert
- Escalate to Tier 2
- Disable account
- Isolate host
- Notify user
- Open incident case

Triage is about decision-making.

---

# What I Learned Today

- Not every alert means compromise.
- Context is everything.
- Correlation is key.
- Parent-child processes are very important.
- A good analyst thinks before reacting.

---

# My Takeaway

Alert triage requires both technical knowledge and judgment.

The goal is not to panic.  
The goal is to analyze calmly, think logically, and make the right decision.
