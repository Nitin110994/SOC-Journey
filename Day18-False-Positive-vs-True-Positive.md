considering the network traffic analysis we performed earlier with malicious xload forbook infection
we shall determine if it was a true positive or false positive alert.


Step 1 — Define the Alert Scenario

In a SOC, alerts usually come from:

SIEM

EDR

Network monitoring tools

Example alert for our case:

Suspicious outbound HTTP communication detected from internal host.

Affected host:

10.9.5.71

Destination:

166.117.110.61

Protocol:

HTTP POST
Step 2 — Possible Explanations

Before jumping to conclusions, SOC analysts consider multiple hypotheses.

Hypothesis 1 – False Positive

Possible legitimate causes:

normal web browsing

software updates

telemetry traffic

automated scripts

Hypothesis 2 – True Positive

Possible malicious causes:

malware beaconing

command-and-control communication

data exfiltration

Step 3 — Evidence Collected During Investigation

From your Wireshark analysis we observed:

Suspicious DNS Queries

Repeated queries for:

www.thealnwickgarden.net

Many responses returned:

No such name
External Communication

Connection from:

10.9.5.71 → 166.117.110.61

Protocol:

TCP port 80
HTTP POST Request

The infected host sent:

POST /fshv/ HTTP/1.1
Host: www.mainenugs.net

POST requests often indicate data being sent to a server.

Encoded Payload

The request contained encoded data:

application/x-www-form-urlencoded

Large encoded payloads often indicate data exfiltration or beaconing.

Persistent Communication

Wireshark conversations showed:

6039 packets exchanged
~3 MB transferred
Duration ~141 minutes

This indicates continuous communication.

Step 4 — Analysis

Now we evaluate the evidence.

Indicators suggesting malicious activity:

repeated DNS resolution attempts

connection to suspicious external server

HTTP POST requests transmitting encoded data

sustained communication with external host

fake browser user-agent

These patterns are typical of malware command-and-control traffic.

Step 5 — Final Decision
Classification: TRUE POSITIVE

The alert represents genuine malicious activity.

Step 6 — Justification
