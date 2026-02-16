

Today I focused on understanding MITRE ATT&CK and how it connects to real SOC alerts.

Before today, I used to just look at logs and think “this looks suspicious.”  
Now I understand that MITRE helps classify attacker behavior in a structured way.

---

## What is MITRE ATT&CK?

MITRE ATT&CK is a framework that shows how attackers behave in real environments.

It helps security teams:
- Understand attack stages
- Categorize alerts
- Improve detection
- Write better incident reports

It is not a tool. It is a knowledge base of attacker techniques.

---

## Two Important Terms

### Tactic
The attacker’s goal.

Examples:
- Initial Access
- Execution
- Persistence
- Credential Access
- Lateral Movement
- Command & Control
- Defense Evasion

### Technique
How the attacker achieves that goal.

Example:
Brute force login → Technique under Credential Access.

---

## How MITRE Connects to SOC Alerts

Here are some examples I learned:

---

### Multiple Failed Logins (Event ID 4625)

If I see many failed login attempts:

This maps to:
- Tactic: Credential Access
- Technique: Brute Force

Reason:
The attacker is trying to guess or force passwords.

---

### Successful Login After Many Failures

This maps to:
- Tactic: Initial Access
- Technique: Valid Accounts

Reason:
The attacker successfully logged in using valid credentials.

---

### Word Spawning PowerShell

If WINWORD.EXE launches powershell.exe:

This maps to:
- Tactic: Execution
- Technique: PowerShell

Reason:
A malicious document might have executed a macro.

If the command is encoded:
- Tactic: Defense Evasion

---

### PowerShell Downloading a File

If PowerShell downloads a file from the internet:

This maps to:
- Tactic: Command & Control
- Technique: Ingress Tool Transfer

Reason:
The attacker is bringing malware into the system.

---

### LSASS Access (Mimikatz Behavior)

If a process accesses LSASS:

This maps to:
- Tactic: Credential Access
- Technique: OS Credential Dumping

Reason:
LSASS stores credentials in memory.

This is a serious post-compromise indicator.

---

### New Local Admin Account Created

This maps to:
- Tactic: Persistence
- Technique: Create Account

Reason:
The attacker wants to maintain access.

---

### Scheduled Task Created

This maps to:
- Tactic: Persistence

Reason:
The malware can run automatically after reboot.

---

### Internal RDP Login

This maps to:
- Tactic: Lateral Movement
- Technique: Remote Services

Reason:
The attacker is moving to another system inside the network.

---

## What I Learned Today

1. MITRE is about attacker behavior, not just log events.
2. One alert can map to multiple tactics.
3. Attackers move in stages.
4. If I see PowerShell + new account + RDP, it is likely post-compromise.

---

## How I Will Use This in SOC Role

When I see an alert, I will:

1. Identify what the attacker is trying to do.
2. Classify the tactic.
3. Identify the technique.
4. Place it in the attack timeline.


