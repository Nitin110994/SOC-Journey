import whois
def check_domain(domain):
    try:
        info = whois.whois(domain)
        return {"domain": domain, "creation_date": info.creation_date, "registrar": info.registrar}
    except Exception as e:
        return {"domain": domain, "creation_date": None, "registrar": None, "error": str(e)}
if __name__ == "__main__":
    print(check_domain("google.com"))
    print(check_domain("this-domain-definitely-does-not-exist-12345.com"))