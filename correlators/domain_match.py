from urllib.parse import urlparse


def correlate_urls_to_subdomains(urls, subdomains):
    """
    Returns mapping:
    {
        subdomain: [url1, url2]
    }
    """
    mapping = {}

    for url in urls:
        try:
            host = urlparse(url).hostname
            if not host:
                continue

            for sub in subdomains:
                if host == sub or host.endswith("." + sub):
                    mapping.setdefault(sub, []).append(url)
        except Exception:
            continue

    return mapping
