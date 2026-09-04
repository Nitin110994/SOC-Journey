import dns.resolver
from permute import domain_variants

# Use reliable public DNS servers instead of the system's (potentially broken) resolv.conf
resolver = dns.resolver.Resolver()
resolver.nameservers = ['8.8.8.8', '1.1.1.1']  # Google + Cloudflare public DNS
resolver.timeout = 2       # per-server timeout
resolver.lifetime = 5      # total budget per query, across both servers

def check_domain(domain):
    """
    Attempts to resolve A, MX, and NS records for a domain.
    Returns a dict of findings, or None if the domain doesn't resolve at all.
    """
    result = {"domain": domain, "a_records": [], "mx_records": [], "ns_records": []}
    resolved = False

    for record_type, key in [("A", "a_records"), ("MX", "mx_records"), ("NS", "ns_records")]:
        try:
            answers = resolver.resolve(domain, record_type)
            result[key] = [str(r) for r in answers]
            resolved = True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers, dns.exception.Timeout):
            continue

    return result if resolved else None


if __name__ == "__main__":
    target_name = "irctc"
    target_suffix = "co.in"

    candidates = domain_variants(target_name, target_suffix)
    print(f"Checking {len(candidates)} candidate domains for live DNS records...\n")

    live_domains = []
    for i, domain in enumerate(sorted(candidates), 1):
        print(f"[{i}/{len(candidates)}] Checking {domain}...", end="\r")
        result = check_domain(domain)
        if result:
            live_domains.append(result)
            print(f"\n  LIVE: {domain} -> A:{result['a_records']} MX:{result['mx_records']}")

    print(f"\n\nDone. Found {len(live_domains)} live domains out of {len(candidates)} checked.")
