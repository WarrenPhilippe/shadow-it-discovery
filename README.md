# 🕵️ Shadow IT Discovery

*Finding the stuff nobody remembers — before attackers do.*

Shadow IT Discovery is a **passive reconnaissance tool** designed to uncover **unmonitored, forgotten, or ignored IT assets** that organisations *swear* don’t exist anymore.

No scanning.
No exploits.
No red‑team cowboy stuff.

Just **what the internet already knows**.

> If Google can see it, attackers can too — and they don’t need permission.

---

## 🔍 What This Tool Actually Does

Shadow IT Discovery combines:

* **Google Dorking** – yes, still alive, yes, still dangerous
* **Passive Subdomain Enumeration** – Amass & Subfinder doing the boring work
* **Certificate Transparency** – because TLS logs don’t lie (but they also don’t tell the full story)
* **Correlation & Scoring** – turning “random URLs” into “things you should worry about”

The output highlights:

* Forgotten login portals
* Legacy mobile applications
* Admin & management interfaces
* Vendor-hosted platforms nobody monitors
* Stuff that never made it into your CMDB

---

## 🧠 Why This Exists

Security teams rely heavily on:

* Asset inventories
* DNS records
* Cloud dashboards
* Certificate Transparency logs

Attackers rely on:

* Google
* Curiosity
* Neglect

Guess who wins most of the time?

---

## ⚙️ Installation

### Requirements

* Python **3.9+**
* Linux / macOS (Windows users… you’re brave)
* Go (for Amass & Subfinder)

---

### Clone the Repo

```bash
git clone https://github.com/WarrenPhilippe/shadow-it-discovery.git
cd shadow-it-discovery
```

---

### Python Environment (because dependency chaos is real)

```bash
python3 -m venv shadow-it-discovery_env
source shadow-it-discovery_env/bin/activate
pip install -r requirements.txt
```

---

### Install External Tools

#### Amass

```bash
go install -v github.com/owasp-amass/amass/v4/...@latest
```

#### Subfinder

```bash
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

Make sure `$GOPATH/bin` is in your `$PATH`, unless you enjoy debugging for no reason.

---

## ▶️ Usage

Basic run:

```bash
python3 discover.py -d example.com
```

Verbose (for people who enjoy logs):

```bash
python3 discover.py -d example.com -v
```

---

## ⚖️ Is This Legal?

Yes.
Very.
Boringly so.

See the Wiki page: **Why This Is Legal**.

---

## 🎯 Who This Is For

* Blue teams
* Security consultants
* Risk & compliance folks
* Organisations preparing audits
* Anyone who suspects their asset inventory is lying

---

**Author:**
Jamie Warren Philippe
Senior Cybersecurity Consultant the day, DareDevil by night lol!
Mauritius 🇲🇺

*“I Google things professionally.”*
