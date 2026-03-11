SOC Investigation – Phishing Email Analysis


1. Alert Summary
   
A suspicious email was detected in the user's spam folder claiming that the user's cloud storage account had been blocked and their data would be deleted unless payment information was updated.
The email attempts to create urgency and redirect the user to update payment details.


3. Email Metadata Analysis
From the header:
sender name
nitinraj1109

Sender email
alert-6087@1pgha.mail.store.bss0007.prooutersys.biz.ua
me@1pgha.io

Subject
We've Blocked Your Account! Your photos and videos will be deleted
Key Finding

The sender domain is extremely suspicious:
prooutersys.biz.ua


Indicators:
Random subdomains
Unrelated to any legitimate cloud provider
Uses .ua domain with multiple nested subdomains
This is a common phishing infrastructure pattern.



3. Social Engineering Indicators
The email uses multiple psychological tactics.
Urgency
Urgent: Action Required
Fear
Your photos and videos will be deleted
Time Pressure
Final reminder
Financial Trigger
Update payment information
These are classic phishing psychological triggers.


4. Brand Impersonation
The email claims to be related to a cloud storage service.
However:
No real company name
Generic term "Cloud"
No official domain
Legitimate services (Google, Apple, Microsoft) always send from official domains.


5. Suspicious Link
The email contains a button:
Update Payment & Secure My Data
This would typically redirect to a credential harvesting or payment phishing page.

SOC rule:
⚠️ Never click links directly.
Instead we extract the URL and analyze it using reputation tools.


6. Email Authentication Indicators
From the header we see:
mailed-by: store.bss0007.prooutersys.biz.ua
This domain is not associated with any major provider.

Likely indicators:
Check	Result
SPF	Likely Fail
DKIM	Likely Missing
DMARC	Likely Fail
This strongly suggests spoofing.


7. Indicators of Compromise (IOCs)
Domain:
prooutersys.biz.ua
Subdomain:
1pgha.mail.store.bss0007.prooutersys.biz.ua
Sender Email:
alert-6087@1pgha.mail.store.bss0007.prooutersys.biz.ua

Subject:
We've Blocked Your Account


8. MITRE ATT&CK Mapping
Mapped to MITRE ATT&CK
Tactic	Technique
Initial Access	Phishing (T1566)
Credential Access	Credential Harvesting
Defense Evasion	Domain spoofing


10. Risk Assessment
If the user clicks the link:
Possible outcomes:
Credential theft
Credit card theft
Malware download
Account takeover
Severity level:
Medium–High


10. SOC Response Actions
Recommended actions:
Block the sender domain in the email gateway
Add domain to threat intelligence block list
Search organization mail logs for similar emails
Notify users about phishing campaign
Monitor authentication logs for suspicious logins

11. Final Conclusion

The email is confirmed to be a phishing attempt designed to trick users into updating payment information through a malicious link.
The attacker uses urgency, fear, and impersonation tactics to manipulate the victim.

The email was correctly detected by the spam filter and did not result in user interaction.
