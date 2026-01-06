#!/usr/bin/env python3

import argparse
import sys

from collectors.google_serp import query_google_serp, extract_urls
from collectors.amass import run_amass
from collectors.subfinder import run_subfinder
from collectors.crtsh import run_crtsh
from correlators.domain_match import correlate_urls_to_subdomains
from scoring.risk import score_assets


API_KEY_FILE = "project_keys/x-api-key"


def read_api_key():
    try:
        with open(API_KEY_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"[!] Missing API key file: {API_KEY_FILE}", file=sys.stderr)
        sys.exit(1)


def build_shadow_it_dork(domain):
    indicators = [
        "login", "signin", "auth", "sso", "oauth",
        "admin", "administrator", "manage",
        "portal", "dashboard",
        "internal", "intranet", "employee", "staff",
        "hr", "finance", "billing",
        "mobile", "m", "wap",
        "legacy", "old",
        "dss", "ff",
        "api", "graphql", "swagger",
        "dev", "test", "staging", "beta",
        ".aspx", ".php", ".jsp", ".do"
    ]

    joined = " OR ".join(indicators)
    return f"inurl:{domain} ({joined})"


def main():
    parser = argparse.ArgumentParser(
        description="Shadow IT Discovery Orchestrator"
    )
    parser.add_argument(
        "-d", "--domain",
        required=True,
        help="Target domain (e.g. airmouritius.mu)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v, -vv)"
    )

    args = parser.parse_args()
    domain = args.domain.lower()
    verbosity = args.verbose

    print(f"[*] Starting Shadow IT discovery for: {domain}")

    if verbosity >= 1:
        dork = build_shadow_it_dork(domain)
        print(f"[DEBUG] Google dork: {dork}")

    # ---- Google SERP ----
    api_key = read_api_key()
    dork = build_shadow_it_dork(domain)

    print("\n[*] Querying Google SERP...")
    serp_data = query_google_serp(api_key, dork, verbosity)
    urls = extract_urls(serp_data, verbosity)

    print(f"[+] {len(urls)} URLs discovered via Google")

    # ---- Subdomain Enumeration ----
    print("\n[*] Running Amass...")
    amass_subs = run_amass(domain, verbosity)
    print(f"[+] Amass: {len(amass_subs)} subdomains")

    print("\n[*] Running Subfinder...")
    subfinder_subs = run_subfinder(domain, verbosity)
    print(f"[+] Subfinder: {len(subfinder_subs)} subdomains")

    print("\n[*] Querying crt.sh...")
    crt_subs = run_crtsh(domain, verbosity)
    print(f"[+] crt.sh: {len(crt_subs)} subdomains")

    all_subdomains = amass_subs | subfinder_subs | crt_subs
    print(f"\n[+] Total unique subdomains: {len(all_subdomains)}")

    # ---- Correlation ----
    print("\n[*] Correlating URLs with subdomains...")
    correlated = correlate_urls_to_subdomains(urls, all_subdomains)

    # ---- Risk Scoring ----
    scored = score_assets(correlated)

    print("\n===== SHADOW IT FINDINGS =====\n")

    for sub, data in sorted(
        scored.items(),
        key=lambda x: x[1]["score"],
        reverse=True
    ):
        print(f"[{data['score']:02d}] {sub}")
        for url in data["urls"]:
            print(f"     └─ {url}")

    print("\n[✔] Discovery complete.")


if __name__ == "__main__":
    main()
