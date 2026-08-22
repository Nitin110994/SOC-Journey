# IDS Deployment & Packet Analysis: STRRAT C2 Investigation

I set up Suricata as an IDS on a Kali VM and ran it against a real malicious pcap (from malware-traffic-analysis.net) to practice the kind of triage a SOC L1 analyst actually does: get an alert, then go verify it yourself in Wireshark instead of just trusting the tool.

## What I did

- Installed Suricata and pulled a real ruleset (Emerging Threats Open, ~52,500 rules) using `suricata-update`
- Ran Suricata in offline mode against the pcap: `suricata -r <pcap> -l suricata-logs/`
- Reviewed the alerts it generated, then opened the same pcap in Wireshark to manually verify the traffic behind the alerts — checking source/dest IPs, ports, protocol behavior, and actually following the TCP stream
- Decoded the malware's own C2 protocol (it was sent in plaintext) to pull out real details: malware family, victim hostname/user, and even the victim's active window title being reported back to the attacker
- Checked for the initial infection vector and came up empty within this capture window — documented that honestly instead of guessing

## Files

- `2024-07-30-traffic-analysis-exercise.pcap` — the source pcap I investigated
- `suricata-logs/` — raw Suricata output (fast.log, eve.json, stats.log)
- `incident_report.md` — my full write-up: executive summary, victim details, timeline, IOCs, MITRE ATT&CK mapping, and recommended response

## Key finding

The infected host was beaconing to a C2 server every ~5 seconds, sending host fingerprint data and periodic snapshots of whatever window the victim had open. The C2 IP was also independently flagged on Spamhaus's DROP list, which lined up with what Suricata alerted on separately — two different sources pointing at the same IP.

Full write-up is in `incident_report.md`.
