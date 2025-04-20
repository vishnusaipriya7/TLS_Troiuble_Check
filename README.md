# YouTube Clone

![image](https://github.com/rishiiiidha/youtube-clone/assets/126899168/d52b2aa0-bf71-426d-bbed-1d2127e9be60)

## Project Structure

- `index.html`: The main HTML file defining the video thumbnail display.
- `style.css`: The CSS file providing styling for the video thumbnails.

# 🔐 TLS_Troiuble_Check

This tool helps analyze **SSL/TLS misconfigurations** like:

- Self-signed certificates
- LUCKY13 vulnerability
- Missing HSTS header
- Long certificate validity
- Missing Subject Alternative Names (SANs)

---

## 📁 Project Structure

| File         | Description                                       |
|--------------|---------------------------------------------------|
| `index.html` | Main HTML file displaying video thumbnail         |
| `style.css`  | CSS file for styling the video thumbnail UI       |
| `tls_check.py` | Python script for SSL/TLS analysis using OpenSSL |

---

## 🚀 How to Run This Project (Python Version)

### 🧰 Prerequisites

- Python 3.x installed
- OpenSSL installed
- `pip` installed

---

### ⚙️ Setup & Execution

1. **Clone this repository**
   ```bash
   git clone https://github.com/vishnusaipriya7/TLS_Troiuble_Check.git
   cd TLS_Troiuble_Check
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the script

bash
Copy
Edit
python tls_check.py
Enter the target domain when prompted Example:

nginx
Copy
Edit
Enter domain: https://example.com
Output will include:

🧾 Certificate validity

🔐 Self-signed or trusted cert

❌ Missing HSTS header

📅 Certificate expiration

🧬 Presence of Subject Alternative Names (SANs)

💣 Detection of LUCKY13 (if possible)

🧪 Sample Output
bash
Copy
Edit
[+] Certificate is NOT self-signed ✅  
[+] HSTS header is missing ⚠️  
[+] Certificate will expire in 120 days  
[+] SANs include: www.example.com, example.com  
⚙️ How to Run with testssl.sh (WSL)
This project also supports scanning via testssl.sh on WSL (Windows Subsystem for Linux).

🧰 Prerequisites
Windows 10/11 with WSL enabled

WSL distro (e.g., Ubuntu)

Git installed in WSL

🧪 Setup Instructions
Open WSL (Search "Ubuntu" in Start)

Install Git

bash
Copy
Edit
sudo apt update
sudo apt install git
Clone testssl.sh repo

bash
Copy
Edit
git clone --depth 1 https://github.com/drwetter/testssl.sh.git
cd testssl.sh
chmod +x testssl.sh
Run the scan Replace the target URL with your own:

bash
Copy
Edit
./testssl.sh --fast --nodns https://192.168.56.1:8443
This will:

Skip reverse DNS lookups (--nodns)

Perform a fast scan (--fast)

Output SSL/TLS vulnerabilities


---

## 🎥 Demo

👉 [Click to watch demo](https://www.loom.com/share/97cfafc5a417472ea254ed7aed69e2a0?sid=a2286058-3f88-4cad-93cf-46015172cd8d)


---
## 📑 Presentation

Check out the slides that go along with this project:

🎞️ [View the Presentation](https://www.canva.com/design/DAGfQ6rSwYs/tDsBn6cb-WeZ0bMh0_aObA/edit?ui=eyJIIjp7IkEiOnRydWV9fQ)
---

📝 Notes
testssl.sh doesn't require installation — just clone and run

Use --jsonfile or --htmlfile to export scan reports

For a full deep scan, remove --fast and --nodns options
