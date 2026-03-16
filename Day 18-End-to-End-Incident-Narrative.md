# Day 18 – End-to-End Incident Narrative

## Overview

In this investigation, I analyzed a PCAP file containing network traffic related to a suspected malware infection. The objective was to identify any suspicious behavior, determine whether the activity represented a real security incident, and document the findings.

The analysis was performed using Wireshark.

---

## Initial Observation

I began the investigation by reviewing DNS traffic within the capture. One internal host stood out because it was repeatedly attempting to resolve the domain:

www.thealnwickgarden.net

Many of the DNS responses returned **"No such name"**, which suggested the host was repeatedly trying to reach a domain that was either inactive or blocked.

The source of these queries was identified as:

10.9.5.71

This made the host to put under further investigation.

## DNS Queries

![DNS Query](dns_query_suspicious_domain.png)

---

## Identifying Suspicious Network Communication

After identifying the suspicious host, I filtered all traffic associated with:

10.9.5.71

While reviewing the packets, I noticed the host initiating connections to an external IP address:

166.117.110.61

The connection was established using HTTP over port 80.

External communication like this can sometimes be legitimate, so the next step was to inspect the contents of the communication.

---

## HTTP Traffic Analysis

Within the HTTP traffic, I identified a POST request sent from the internal host to the external server.

The request looked like this:

POST /fshv/ HTTP/1.1  
Host: www.mainenugs.net

POST requests are commonly used to send data to a server. In this case, the request contained a large encoded payload with the content type:

application/x-www-form-urlencoded

This type of behavior is often associated with malware transmitting information to a command-and-control server.

---

## TCP Stream Inspection

To better understand the communication, I followed the TCP stream associated with the POST request.

The stream contained a large block of encoded data that appeared to be transmitted from the infected host to the remote server.

This behavior suggested that the system was likely sending data to an attacker-controlled server.

## TCP Stream Communication

![TCP Stream](tcp_stream_c2_communication.png)

---

## Conversation Analysis

To understand how much communication occurred between the internal host and the external server, I reviewed the conversation statistics in Wireshark.

The analysis showed significant communication between:

Internal host: 10.9.5.71  
External server: 166.117.110.61  

Key details:

Packets exchanged: 6039  
Data transferred: approximately 3 MB  
Communication duration: approximately 141 minutes

The sustained communication over this period strongly suggests persistent command-and-control activity.

## TCP Stream Communication

![TCP Stream](tcp_stream_c2_communication.png)

---

## Indicators of Compromise

During the investigation, the following indicators were identified:

| Indicator | Value |
|---|---|
Infected Host | 10.9.5.71 |
External Server | 166.117.110.61 |
Suspicious Domain | www.mainenugs.net |
HTTP Endpoint | /fshv/ |
Protocol Used | HTTP |

---

## MITRE ATT&CK Techniques

Based on the observed behavior, the activity aligns with the following MITRE ATT&CK techniques:

Command and Control over Web Protocol  
T1071.001

Exfiltration Over Web Services  
T1041

---

## Conclusion

Based on the network traffic analysis, the internal host **10.9.5.71** appears to be infected and attempting to communicate with an external command-and-control server.

The host repeatedly initiated HTTP POST requests to the domain **www.mainenugs.net**, sending encoded data to the external IP **166.117.110.61**.

The repeated communication, encoded payloads, and long-duration connection strongly indicate malicious activity consistent with **XLoader malware behavior**.

For these reasons, this alert was classified as a **true positive security incident**.
