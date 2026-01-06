import requests

def run_crtsh(domain, verbose=False):
    if verbose:
        print(f"[DEBUG] Querying crt.sh for domain: {domain}")

    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        subdomains = set()
        for entry in data:
            name = entry.get("name_value")
            if name:
                for sub in name.split("\n"):
                    subdomains.add(sub.strip())
                    if verbose:
                        print(f"[DEBUG] crt.sh found: {sub.strip()}")
        return subdomains
    except Exception as e:
        print(f"[!] Error querying crt.sh: {e}")
        return set()
