from datetime import datetime, timezone
def determine_verdict(reputation_data, domain_data):
    score = 0
    malicious_count = reputation_data["malicious"]
    if malicious_count >= 5:
        score = score + 5
    elif malicious_count >= 1:
        score = score + 2
    suspicious_count = reputation_data["suspicious"]
    if suspicious_count >= 3:
        score = score + 2
    elif suspicious_count >= 1:
        score = score + 1
    creation_date = domain_data["creation_date"]
    if isinstance(creation_date, list):
        creation_date = creation_date[0]
    if creation_date is not None:
        age_days = (datetime.now(timezone.utc) - creation_date).days     
        if age_days < 30:
            score = score + 3
    if score >= 8:
        verdict = "malicious"
    elif score >= 3:
        verdict = "suspicious"
    else:
        verdict = "likely benign"   
    return {"score": score, "verdict": verdict}                 

if __name__ == "__main__":
    fake_reputation = {"url": "test", "malicious": 11, "suspicious": 3, "harmless": 46}
    fake_domain_new = {"domain": "test", "creation_date": datetime(2026, 8, 10, tzinfo=timezone.utc), "registrar": None}
    print(determine_verdict(fake_reputation, fake_domain_new))