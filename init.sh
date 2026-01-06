#!/usr/bin/env bash

set -e

PROJECT_NAME="shadow-it-discovery"
VENV_DIR="venv"

echo "[*] Initialising $PROJECT_NAME environment..."

# 1️⃣ Create directory structure
echo "[*] Creating project directories..."

mkdir -p collectors correlators scoring project_keys output

touch collectors/__init__.py
touch correlators/__init__.py
touch scoring/__init__.py

# 2️⃣ Create placeholder modules
echo "[*] Creating module placeholders..."

touch collectors/google_serp.py
touch collectors/amass.py
touch collectors/subfinder.py
touch collectors/crtsh.py
touch correlators/domain_match.py
touch scoring/risk.py

# 3️⃣ Create Python virtual environment
if [ ! -d "$VENV_DIR" ]; then
    echo "[*] Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "[*] Virtual environment already exists"
fi

# 4️⃣ Activate virtualenv
echo "[*] Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# 5️⃣ Create requirements.txt if missing
if [ ! -f "requirements.txt" ]; then
    echo "[*] Creating requirements.txt..."
    cat <<EOF > requirements.txt
requests
EOF
fi

# 6️⃣ Install Python dependencies
echo "[*] Installing Python dependencies..."
if [ ! -f "requirements.txt" ]; then
    echo "[*] Creating requirements.txt..."
    cat <<EOF > requirements.txt
requests>=2.31.0
EOF
fi
pip install --upgrade pip
pip install -r requirements.txt

# 7️⃣ API key placeholder
if [ ! -f "project_keys/x-api-key" ]; then
    echo "[*] Creating API key placeholder..."
    touch project_keys/x-api-key
    chmod 600 project_keys/x-api-key
    echo "[!] Add your HasData API key to project_keys/x-api-key"
fi

echo
echo "[✔] Initialisation complete."
echo
echo "Next steps:"
echo "  source venv/bin/activate"
echo "  python3 send_query.py -d example.com"
