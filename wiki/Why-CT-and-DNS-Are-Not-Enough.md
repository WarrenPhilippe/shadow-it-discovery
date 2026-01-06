# ❌ Why Certificate Transparency & DNS Are Not Enough

### Certificate Transparency (crt.sh)

CT logs are useful — but incomplete.

They **do not show**:

* HTTP-only services
* Legacy platforms
* Systems without certificates
* Internal apps never issued TLS

**Example:**

```
http://dss.{REDACTED DOMAIN}.mu/mobile/FFlogin.aspx
```

✔ Public
✔ Indexed by Google
❌ TLS
❌ crt.sh visibility

Blind spot.

---

### DNS Enumeration

DNS tells you *what exists*, not *what is exposed*.

It won’t tell you:

* Which paths are indexed
* Which URLs expose authentication
* Which systems attackers actually see

DNS needs context.
Google provides it.
