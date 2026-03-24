# Detection Improvement Proposal: Brute Force Detection

## Current Limitation
The current rule only detects fast brute force attacks within a short time.

It may miss:
- Slow attacks
- Attacks from multiple IP addresses

---

## Proposed Improvements

### 1. Detect Slow Attacks
Increase the time window.

Example:
IF failed_logins > 20 within 30 minutes  
THEN trigger alert

---

### 2. IP-Based Detection
Detect multiple accounts targeted from the same IP.

Example:
IF multiple accounts fail login from same IP  
THEN trigger alert

---

### 3. Detect Success After Failure
Check if a successful login happens after multiple failures.

Example:
IF failed_logins followed by successful_login  
THEN trigger high severity alert

---

### 4. Add Threat Intelligence
Check if the IP is malicious using threat intelligence.

---

### 5. Geo-Location Check
Detect login from unusual locations.

Example:
IF login location is different from usual  
THEN trigger alert

---

## Expected Outcome
- Better detection of advanced attacks
- Reduced missed attacks
- Improved SOC visibility

---

## Insight
Combining multiple detection methods helps reduce both false positives and false negatives.



## Insight
If failed login attempts are followed by a successful login, it may indicate that the attacker guessed the password successfully.
