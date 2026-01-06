import subprocess

def run_subfinder(domain, verbose=False):
    if verbose:
        print(f"[DEBUG] Running Subfinder for domain: {domain}")

    try:
        result = subprocess.run(
            ["subfinder", "-d", domain, "-silent"],
            capture_output=True,
            text=True
        )
        subdomains = set(result.stdout.splitlines())
        if verbose:
            print(f"[DEBUG] Subfinder found: {len(subdomains)} subdomains")
        return subdomains
    except FileNotFoundError:
        print("[!] Subfinder not installed or not in PATH")
        return set()
