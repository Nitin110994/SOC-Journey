def generate_report(email_data, iocs, rep_result, domain_result, verdict):
    report = f"""# Phishing Investigation Report

## Email Details
- Sender: {email_data['sender']}
- Subject: {email_data['subject']}
"""
    report += f"""
## IOCs Found
- URLs: {iocs['urls']}
- Emails: {iocs['emails']}
- IPs: {iocs['ips']}
"""

    report += f"""
## Reputation Check
- URL: {rep_result.get('url', 'N/A')}
- Malicious detections: {rep_result.get('malicious', 'N/A')}
- Suspicious detections: {rep_result.get('suspicious', 'N/A')}
"""
    report += f"""
## Domain Analysis
- Domain: {domain_result.get('domain', 'N/A')}
- Creation Date: {domain_result.get('creation_date', 'N/A')}
- Registrar: {domain_result.get('registrar', 'N/A')}
"""
    report += f"""
## Final Verdict
- Score: {verdict['score']}
- Classification: {verdict['verdict'].upper()} 
"""
    return report 