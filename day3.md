SPLUNK hands on

created an access.log file
27.0.0.1 - - [26/Nov/2025:10:00:00 +0530] "GET /login HTTP/1.1" 200 532 "-" "Mozilla/5.0"
127.0.0.1 - - [26/Nov/2025:10:00:05 +0530] "POST /login HTTP/1.1" 401 123 "-" "Mozilla/5.0"
10.0.0.5 - - [26/Nov/2025:10:01:00 +0530] "GET /admin HTTP/1.1" 403 231 "-" "Mozilla/5.0"
192.168.1.10 - - [26/Nov/2025:10:02:30 +0530] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0"
10.0.0.5 - - [26/Nov/2025:10:03:20 +0530] "POST /login HTTP/1.1" 401 332 "-" "Mozilla/5.0"
10.0.0.5 - - [26/Nov/2025:10:03:30 +0530] "POST /login HTTP/1.1" 401 198 "-" "Mozilla/5.0" 

and was able to search logs in Splunk, write basic SPL for SOC use-case, and save a search (report/alert or dashboard panel).

1. Data Ingestion
Added log file using:
Settings → Add Data → Upload
Configuration:
sourcetype: access_combined
Index: main

2.Basic Search
index=main
Result: 6 events loaded successfully.

📸 Screenshot: index=main search results
<img width="1839" height="875" alt="Screenshot 2025-11-27 105548" src="https://github.com/user-attachments/assets/3f6a9186-89da-469a-88a1-a6fe688aaf93" />

3. Search Failed Login Attempts
index=main "/login" status=401


4. Count Failed Logins by IP
index=main "/login" status=401
| stats count BY clientip
| sort - count

Result
clientip	count
10.0.0.5	2
127.0.0.1	1

📸 Screenshot: stats count BY clientip
<img width="1833" height="730" alt="Screenshot 2025-11-27 105816" src="https://github.com/user-attachments/assets/57e6a580-745c-40ad-ac5d-300a1407bfe8" />


5. Apply Suspicious Threshold (Brute Force Detection)
index=main "/login" status=401
| stats count BY clientip
| where count >= 2
| sort - count

Suspicious IP identified
10.0.0.5


📸 Screenshot
<img width="1507" height="606" alt="Screenshot 2025-11-27 110540" src="https://github.com/user-attachments/assets/63554d7f-92b5-43d4-8aa5-af766afa54bf" />


6. Analyze /admin Access Attempts
index=main "/admin"
| stats count BY clientip
| sort - count


Result:

10.0.0.5 = 1 access


📸 Screenshot
<img width="1894" height="577" alt="image" src="https://github.com/user-attachments/assets/5ff36e83-2467-459f-8d0a-f0c7e4bb8974" />

7. Attacker Behavior Correlation
index=main clientip=10.0.0.5
| stats count BY uri status
| sort uri status

Outcome
uri	status	count
/login	401	2
/admin	403	1

📸 Screenshot
<img width="1883" height="467" alt="image" src="https://github.com/user-attachments/assets/df64d4cd-79bb-4f67-9a91-c23ada0b5a2b" />


8. Create Alert (Brute Force Detection)
Save As → Alert
Title: Possible Brute Force Login
Type: Scheduled (Hourly)
Trigger when: Number of results > 0


📸 Screenshot
<img width="1180" height="757" alt="image" src="https://github.com/user-attachments/assets/455549c3-a5a5-4acd-bc3b-6080eb17d1be" />


9. Build Dashboard

Dashboard Name:

Web Security Overview

Panel 1 – HTTP Status Code Breakdown
index=main
| stats count BY status
| sort -count

Panel 2 – Failed Logins by IP
index=main "/login" status=401
| stats count BY clientip
| sort -count


📸 Screenshot: Dashboard with Pie Chart & Table
<img width="1875" height="783" alt="Screenshot 2025-11-27 185028" src="https://github.com/user-attachments/assets/b4f4bb5f-6079-453d-910c-379c54442c2b" />

***Detected suspicious activity originating from IP 10.0.0.5 involving multiple failed login attempts and unauthorized access to /admin endpoint.

Evidence:
- Failed login attempts: 2 (401)
- /admin access attempts: 1 (403)
- Pattern visualized in dashboard and confirmed via correlation search

Actions Taken:
- Created 'Possible Brute Force Login' alert to monitor future attempts
- Built dashboard panels to track login failures and status codes

