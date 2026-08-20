# Phishing Email Investigator

I built this project to automate something I used to do manually — investigating phishing emails as part of a SOC analyst workflow. I started with a manual writeup of a real phishing email (checking headers, IOCs, sender domain, etc.) and then built this tool to do the same investigation automatically using Python.

## What it does

You give it a `.eml` file, and it will:
- Read the email and pull out the sender, subject, and body
- Find any URLs, email addresses, and IPs in the email using regex
- Defang the URLs so they're safe to share in a report
- Check the URL against VirusTotal to see if it's been flagged by other security vendors
- Look up the domain's WHOIS info (when it's created, who registered it)
- Score everything and decide if the email is malicious, suspicious, or likely benign
- Save all of this as a Markdown report

## How to run it

Install the requirements:
```bash
pip install -r requirements.txt
```

You need a free VirusTotal API key (sign up at virustotal.com). Create a `.env` file in the project folder:

VT_API_KEY=your_key_here


Then run:
```bash
python investigate.py path/to/email.eml
```

The report gets saved to `reports/case_report.md`.

## Files in this project

- `email_parser.py` — reads the .eml file
- `ioc_extractor.py` — pulls out URLs/emails/IPs using regex
- `defang.py` — makes URLs safe to display
- `domain_analysis.py` — WHOIS lookup for the domain
- `reputation.py` — checks the URL against VirusTotal
- `verdict_engine.py` — scores everything and gives a final verdict
- `report_generator.py` — builds the Markdown report
- `investigate.py` — runs the whole thing end to end

## Things I know are limitations right now

- It only checks the first URL it finds, not every URL in the email
- Some domains (like `.appspot.com`) don't return WHOIS data from the server I'm using, so domain age doesn't count for those
- VirusTotal's free API has rate limits

## What I might add later

- Check every URL found, not just the first one
- Add DNS lookups
- Let it process multiple emails at once