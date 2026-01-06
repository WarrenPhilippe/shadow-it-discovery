import subprocess

def run_amass(domain, verbose=False):
    if verbose:
        print(f"[DEBUG] Running Amass for domain: {domain}")

    try:
        result = subprocess.run(
            ["amass", "enum", "-d", domain, "-passive"],
            capture_output=True,
            text=True
        )
        subdomains = set(result.stdout.splitlines())
        if verbose:
            print(f"[DEBUG] Amass found: {len(subdomains)} subdomains")
        return subdomains
    except FileNotFoundError:
        print("[!] Amass not installed or not in PATH")
        return set()
