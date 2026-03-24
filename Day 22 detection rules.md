# Detection Engineering Basics

## What is a Detection Rule?
A detection rule is a condition that analyzes logs and triggers an alert when suspicious activity is identified.

## Types of Detection
- Signature-based: Detects known attack patterns.
- Behavior-based: Detects suspicious actions like multiple failed logins.
- Anomaly-based: Detects unusual behavior compared to normal activity.

## Example Detection Rules
- IF failed_logins > 5 within 2 minutes → Possible brute force attack
- IF login from new location → Suspicious login
- IF user becomes admin → Privilege escalation alert

## Log Sources
- Windows Event Logs
- Firewall Logs
- Authentication Logs
- Web Server Logs

## Key Concepts
- False Positive: Alert but no real attack
- False Negative: Attack but no alert


<img width="1247" height="659" alt="Screenshot 2026-03-24 094454" src="https://github.com/user-attachments/assets/23623a13-0c90-4fad-b5ae-0af084d8b1e9" />
Behaviour based detection

## Why Detection Matters
Detection helps identify attacks early so that security teams can respond quickly and prevent damage.

## Insight
Multiple failed login attempts in a short time can indicate a brute force attack and should be monitored closely.
