from report_generator import generate_report
from urllib.parse import urlparse
from reputation import check_url_reputation
from domain_analysis import check_domain
from verdict_engine import determine_verdict
from email_parser import parse_email
from ioc_extractor import extract_iocs
import sys
if len(sys.argv) < 2:
    print("Usage: python investigate.py <path_to_eml_file>")
    sys.exit(1)
filename = sys.argv[1]
email_data = parse_email(filename)  
iocs = extract_iocs(email_data["body"])
first_url = iocs["urls"][0]
parsed = urlparse(first_url)
domain = parsed.netloc
rep_result = check_url_reputation(first_url)
domain_result = check_domain(domain)
#print("Reputation raw:", rep_result)
#print("Domain raw:", domain_result)
verdict = determine_verdict(rep_result, domain_result)
report_text = generate_report(email_data, iocs, rep_result, domain_result, verdict)
with open("reports/case_report.md", "w") as f:
    f.write(report_text)
print("Sender:", email_data["sender"])
print("Subject:", email_data["subject"])
print("IOCs found:", iocs)
print("Investigated URL:", first_url)
print("Verdict:", verdict)