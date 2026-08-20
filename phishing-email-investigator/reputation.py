import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

def check_url_reputation(url):
    try:
        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        headers = {"x-apikey": API_KEY}
        response = requests.get(f"https://www.virustotal.com/api/v3/urls/{url_id}", headers=headers)
    

        if response.status_code == 200:
            data = response.json()
            stats = data["data"]["attributes"]["last_analysis_stats"]
            return {"url": url, "malicious": stats["malicious"], "suspicious": stats["suspicious"], "harmless": stats["harmless"]}
        else:
            return {"url": url, "error": f"VirusTotal returned status {response.status_code}"}
    except requests.exceptions.RequestException as e: 
        return {"url": url, "error": f"Request failed: {str(e)}"}
if __name__ == "__main__":
    result = check_url_reputation("http://testsafebrowsing.appspot.com/s/malware.html")
    print(result)