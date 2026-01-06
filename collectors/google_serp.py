import http.client
import json
import urllib.parse
import sys

HASDATA_HOST = "api.hasdata.com"


def query_google_serp(api_key, query, verbosity=0):
    """
    Query Google SERP via HasData API.

    Verbosity levels:
      0 = silent
      1 = logical steps
      2 = deep debug
    """

    if verbosity >= 1:
        print("[*] Google SERP query prepared")

    encoded_query = urllib.parse.quote(query, safe="")

    if verbosity >= 2:
        print(f"[DEBUG] Raw dork: {query}")
        print(f"[DEBUG] Encoded dork: {encoded_query}")

    conn = http.client.HTTPSConnection(HASDATA_HOST)

    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }

    path = f"/scrape/google/serp?q={encoded_query}&deviceType=desktop"

    if verbosity >= 2:
        print(f"[DEBUG] Request path: {path}")

    try:
        conn.request("GET", path, headers=headers)
        response = conn.getresponse()
        raw_data = response.read()

        if response.status != 200:
            print(f"[!] Google SERP HTTP {response.status}", file=sys.stderr)
            return {}

        data = json.loads(raw_data)

        if verbosity >= 2:
            print(f"[DEBUG] SERP response keys: {list(data.keys())}")

        return data

    except Exception as e:
        print(f"[!] Google SERP failed: {e}", file=sys.stderr)
        return {}

    finally:
        conn.close()


def extract_urls(serp_json, verbosity=0):
    urls = set()
    organic = serp_json.get("organicResults", [])

    if verbosity >= 1:
        print(f"[+] Google SERP returned {len(organic)} results")

    for r in organic:
        link = r.get("link")
        if link:
            urls.add(link)
            if verbosity >= 2:
                print(f"[DEBUG] URL: {link}")

    return urls
