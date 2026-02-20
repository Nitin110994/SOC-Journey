# Day 13 – Attack Timeline Analysis Practice


Today I practiced reconstructing an attack timeline based on simulated log events.

The goal was to understand how to connect individual alerts into a complete attack story.

---

# Why Timeline Analysis is Important

In a SOC environment, alerts come separately.

But attackers operate in stages.

Timeline analysis helps answer:

- What happened first?
- How did the attacker progress?
- When did compromise escalate?
- What actions were taken after access?

Instead of looking at logs individually, I arranged them chronologically to see the full attack flow.

---

# Simulated Investigation Scenario

# Step 1 – Organizing by Time

The first step in timeline analysis is sorting events chronologically.

This helps identify the attack progression.

---

# Step 2 – Mapping Each Event to MITRE

| Time  | Event | MITRE Tactic |
|-------|--------|--------------|
| 09:10 | Multiple failed logins | Credential Access |
| 09:12 | Successful login | Initial Access |
| 09:14 | PowerShell execution | Execution |
| 09:15 | External IP communication | Command & Control |
| 09:17 | Admin account creation | Persistence |
| 09:20 | Internal RDP login | Lateral Movement |


# Attack Progression Flow

The attack progressed in the following order:

Brute Force  
→ Successful Login  
→ PowerShell Execution  
→ External Communication  
→ Persistence Established  
→ Lateral Movement

This shows a clear transition from initial compromise to expansion inside the network.

# Risk Assessment

This timeline indicates post-compromise activity.

The attacker:
- Successfully authenticated
- Executed code
- Established persistence
- Moved laterally

This would be considered a high-severity incident in a real SOC environment.

---

# Key Learnings

- Logs must be analyzed in sequence.
- One alert rarely tells the full story.
- MITRE mapping helps identify attack stages.
- Timeline reconstruction makes incident reports clearer.
- Lateral movement indicates escalation.

---

# Skills Practiced

- Event correlation
- Chronological analysis
- MITRE ATT&CK mapping
- Attack progression understanding
- Incident documentation
