import re
def extract_iocs(text):
    urls = re.findall(r"https?://\S+", text)
    cleaned_urls = []
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    ips = re.findall(r"\d+\.\d+\.\d+\.\d+", text)
    for url in urls:
        cleaned = url.rstrip(".,;:!?)")
        cleaned_urls.append(cleaned)
    return {"urls": cleaned_urls, "emails": emails, "ips": ips}
if __name__ == "__main__":
    result = extract_iocs("Click here http://evil-site.com/login. Also see https://another-fake.com, and http://third-one.com! Contact fake@phisher-site.biz.ua or check IP 192.168.1.1")
    print(result)