RISK_KEYWORDS = {
    "login": 3,
    "admin": 4,
    "portal": 2,
    "dashboard": 2,
    "mobile": 2,
    "legacy": 4,
    "test": 3,
    "dev": 3,
    "staging": 3,
    ".aspx": 4,
    ".php": 3,
    ".jsp": 3
}


def score_url(url):
    score = 0
    lower = url.lower()

    for keyword, weight in RISK_KEYWORDS.items():
        if keyword in lower:
            score += weight

    return score


def score_assets(mapping):
    """
    Input:
      { subdomain: [urls] }

    Output:
      { subdomain: { "score": X, "urls": [...] } }
    """
    scored = {}

    for sub, urls in mapping.items():
        total = sum(score_url(u) for u in urls)
        scored[sub] = {
            "score": total,
            "urls": urls
        }

    return scored
