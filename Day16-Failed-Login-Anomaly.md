# Day 16 – Failed Login Anomaly Detection

## Objective

Understand how SOC teams detect suspicious authentication activity by analyzing failed login attempts and designing detection logic for potential brute force attacks.

---

## Scenario

A security monitoring system detected multiple failed login attempts targeting a single user account within a short time window.

This pattern may indicate a brute force attempt where an attacker repeatedly tries different passwords to gain access.

---

## Example Log Events

Example authentication logs:

User: admin  
Source IP: 192.168.1.45  

```
Failed login attempt for user admin
Failed login attempt for user admin
Failed login attempt for user admin
Failed login attempt for user admin
Failed login attempt for user admin
```

Total failed attempts: **5+ within a few minutes**

---

## Detection Logic

SOC teams often implement SIEM detection rules to identify this behavior.

Example detection logic:

```
IF failed_login_attempts > 5
FROM same IP
WITHIN 5 minutes
THEN trigger alert
```

Eg pesudocode:

```
count(failed_logins) > 5
group by source_ip
within 5 minutes
```

---

## Investigation Steps

When this alert is triggered, a SOC analyst performs the following investigation steps:

1. Identify the user account being targeted.
2. Review the number of failed login attempts.
3. Check the source IP address of the login attempts.
4. Determine whether the login attempts originate from an unusual location.
5. Check if a successful login occurred after the failed attempts.
6. Escalate the incident if suspicious activity is confirmed.

---

## Indicators of Suspicious Activity

Indicators suggesting a brute force attempt:

- Multiple failed logins within a short timeframe
- Login attempts from a single IP address
- Targeting of privileged accounts
- Failed attempts followed by successful login

---

## MITRE ATT&CK Mapping

Technique: **Brute Force**

ID: **T1110**

Description:  
Adversaries may attempt to gain access to accounts by guessing passwords through repeated login attempts.

---

## Conclusion

The failed login anomaly detection rule identifies suspicious authentication activity that may indicate a brute force attack.

By monitoring authentication logs and implementing detection logic, SOC teams can quickly identify and respond to potential account compromise attempts.
