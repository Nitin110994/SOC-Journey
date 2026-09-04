import json
import socket
import ssl
import whois
from datetime import datetime, timezone
from scanner import check_domain
from permute import domain_variants


def get_registration_age_days(domain):
    """Returns days since registration, or None if WHOIS lookup fails."""
    try:
        w = whois.whois(domain)
        created = w.creation_date
        if isinstance(created, list):
            created = created[0]
        if created is None:
            return None
        if created.tzinfo is None:
            created = created.replace(tzinfo=timezone.utc)
        age = (datetime.now(timezone.utc) - created).days
        return age
    except Exception:
        return None


def has_ssl_cert(domain, timeout=3):
    """Checks if the domain has a valid SSL certificate on port 443."""
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=timeout) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.getpeercert() is not None
    except Exception:
        return False


def score_domain(finding):
    """
    Scores a live domain finding based on risk indicators.
    Higher score = more likely to be an active phishing threat.
    """
    domain = finding["domain"]
    score = 0
    reasons = []

    # MX records = can send/receive email = phishing-ready
    if finding["mx_records"]:
        score += 40
        reasons.append("Has MX records (email-capable)")

    # SSL cert = looks more legitimate/production-ready
    if has_ssl_cert(domain):
        score += 20
        reasons.append("Has valid SSL certificate")

    # Registration age
    age_days = get_registration_age_days(domain)
    if age_days is not None:
        if age_days < 30:
            score += 40
            reasons.append(f"Registered very recently ({age_days} days ago)")
        elif age_days < 90:
            score += 25
            reasons.append(f"Registered recently ({age_days} days ago)")
        elif age_days < 365:
            score += 10
            reasons.append(f"Registered within the past year ({age_days} days ago)")
    else:
        reasons.append("Registration age unknown (WHOIS lookup failed/privacy-protected)")

    finding["risk_score"] = score
    finding["registration_age_days"] = age_days
    finding["risk_reasons"] = reasons
    return finding


if __name__ == "__main__":
    target_name = "irctc"
    target_suffix = "co.in"

    candidates = domain_variants(target_name, target_suffix)
    print(f"Scanning {len(candidates)} candidates...\n")

    live_domains = []
    for domain in sorted(candidates):
        result = check_domain(domain)
        if result:
            live_domains.append(result)

    print(f"Found {len(live_domains)} live domains. Scoring each...\n")

    scored_results = []
    for finding in live_domains:
        print(f"Scoring {finding['domain']}...")
        scored = score_domain(finding)
        scored_results.append(scored)
        print(f"  -> Risk score: {scored['risk_score']} | {', '.join(scored['risk_reasons'])}\n")

    # Sort by risk score, highest first
    scored_results.sort(key=lambda x: x["risk_score"], reverse=True)

    import datetime

    log_path = "/var/log/typosquat-scan.log"
    scan_timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    with open(log_path, "a") as f:
        for finding in scored_results:
            finding["scan_timestamp"] = scan_timestamp
            finding["target_domain"] = f"{target_name}.{target_suffix}"
            f.write(json.dumps(finding) + "\n")

    print(f"Done. Results appended to {log_path}")
    print("\n=== TOP RISK DOMAINS ===")
    for r in scored_results[:5]:
        print(f"{r['domain']} - Score: {r['risk_score']}")
