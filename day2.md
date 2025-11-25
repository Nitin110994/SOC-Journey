# 🛡️ Day 2 — Windows Event Logs + Microsoft Defender XDR

This folder contains structured SOC Analyst notes for Day 2.

Topics covered:
- Windows Event Logs overview  
- Important Event IDs  
- Detection use cases  
- Defender XDR incidents  
- Alerts & evidence analysis  
- Automated investigations  
- Advanced Hunting (KQL)  
- SOC alert workflow & severity levels  

# 🪵 1. Windows Event Logs — Overview

Windows Event Logs are a SOC analyst’s **first line of defense**.  
They reveal:
- Unauthorized access attempts  
- Privilege escalation  
- Malware execution  
- Lateral movement  
- File/registry manipulation  
- Scheduled tasks  
- Persistence and log tampering  

---

## 🔍 Important Event IDs (SOC-Focused)

### **Authentication (Logon/Logoff)**
| Event ID | Meaning |
|---------|---------|
| **4624** | Successful login |
| **4625** | Failed login |
| **4647** | Logoff |
| **4634** | Logoff |
| **4675** | Object permission used |

### **Logon Types**  
- Type 2 — Interactive login  
- Type 3 — Network logon  
- Type 4 — Batch (scheduled tasks)  
- Type 7 — Screen unlock  
- Type 10 — RDP  
- Type 11 — Cached creds  

---

### **Account Management**
| Event ID | Action |
|---------|--------|
| **4720** | Account created |
| **4722** | Account enabled |
| **4724** | Password reset |
| **4728/4732/4756** | User added to local/privileged groups |

---

### **Scheduled Tasks**
| Event ID | Action |
|---------|--------|
| 4697 | Task created |
| 4702 | Task updated |
| 4699 | Task deleted |
| 140 | Task in scheduler logs |

---

### **Service Activity**
| Event ID | Action |
|---------|--------|
| 7045 | Service installed |
| 7034 | Service crashed |
| 7040 | Service start type changed |
| 7036 | Service started/stopped |

---

### **Network Activity**
| Event ID | Meaning |
|---------|---------|
| 5140 | Network share accessed |

---

### **Log Manipulation Events**
| Event ID | Meaning |
|---------|---------|
| 1102 | Security log cleared |
| 104 | Audit log cleared |

---

# 🛑 2. Detecting Malicious Activity Using Windows Logs

### ✔ Set up alerts in SIEM  
### ✔ Automate incident response  
### ✔ Correlate multiple event IDs  

Common correlation examples:
- **4625 (failed logins) + 4624 (successful login)** → Bruteforce success  
- **4697 (scheduled task create) + 7045 (service install)** → Persistence  
- **1102 (logs cleared)** → Attacker covering tracks  
- **7045 + unsigned EXE path** → Malware service  

---

# 🎯 3. Tips for Threat Detection in Windows Logs

1. Create **custom SIEM rules**  
2. Enrich logs with **Threat Intel (MISP, VirusTotal)**  
3. Detect lateral movement (IDs **4648, 4624, 4672, 4698**)  
4. Enable **File Integrity Monitoring (FIM)**  
5. Turn on **Advanced Auditing** (Group Policy)  
6. Regularly update detection rules and review logs  

---

# 🛡️ 4. Microsoft Defender XDR — Overview

Microsoft XDR provides:
- Cross-product alert correlation  
- Incident aggregation  
- Single pane view for SOC analysts  
- AI-driven automated investigation  
- MITRE ATT&CK mapping  

---

# 📁 5. XDR Incidents Page Breakdown

### Incident view shows:
- Severity  
- Categories  
- Detection sources  
- Active alerts  
- Impacted devices  
- Impacted users  
- Evidence  

### Example:
- **2/47 active alerts**  
- **9 impacted devices**  
- **5 impacted users**  
- **1 impacted mailbox**  
- **8 MITRE Tactics involved**  

---

# 🚨 6. Alerts — Severity Levels

### **High (Red)**
- Credential theft tools  
- Ransomware  
- Tampering with security sensors  
- Rare, high-impact attack behavior  

### **Medium (Orange)**
- Suspicious command execution  
- Exploit attempt  
- Suspicious script or process behavior  

### **Low (Yellow)**
- Hack tools  
- Enumeration  
- Discovery commands  
- Clearing logs  

---

# 📝 7. Alert Classification Flow

**Alert → Validate → Investigate → Enrich → Decide Severity → Document → Escalate**

Examples:
- Enrich with KQL  
- Validate user sign-in logs  
- Decide if True Positive / Benign  
- Escalate to IR team if needed  

---

# 🔍 8. Evidence Analysis

Evidence includes:
- Files  
- Processes  
- Network connections  
- Emails  
- User activity  
- Registry modifications  

Example:
- `dragonfolder_sow_06132020.doc`  
- Verdict: **Remediated**  
- Device: `barbaram-pc`  
- File quarantined successfully  

---

# 🤖 9. Automated Investigations (AI + Automation)

Types:
### **Full Automation**
- No approval needed  
- Temporary folders (AppData, Temp, Downloads)  
- Immediate remediation  

### **Semi-Automation**
- Approval needed if:
  - File is outside temp folders  
  - Critical system areas involved  

Examples of temporary paths:
- `\users\*\appdata\local\temp*`  
- `\windows\temp*`  
- `\users\*\downloads*`  

---

# 🕵️ 10. Advanced Hunting (KQL)

### Example query shown:
```kql
let selectedTimestamp = datetime(2020-06-14T00:13:59.0000000Z);
let fileName = "dragonfolder_sow_06132020.doc";
let fileSha1 = "de0e86ce91273200b83382a5b404bbe80ddcee86";
search in (DeviceFileEvents, EmailAttachmentInfo, AppFileEvents)
Timestamp between ((selectedTimestamp - 1h) .. (selectedTimestamp + 1h))
and FileName =~ fileName
