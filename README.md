# YouTube Clone

![image](https://github.com/rishiiiidha/youtube-clone/assets/126899168/d52b2aa0-bf71-426d-bbed-1d2127e9be60)

## Project Structure

- `index.html`: The main HTML file defining the video thumbnail display.
- `style.css`: The CSS file providing styling for the video thumbnails.
## 🚀 How to Run This Project

> 🔍 This tool helps you analyze SSL/TLS misconfigurations like self-signed certs, LUCKY13, missing HSTS, long certificate validity, and no SANs using OpenSSL and Python.

### 🧰 Prerequisites

- Python 3.x installed
- OpenSSL installed
- `pip` for installing dependencies

---

### ⚙️ Setup & Run Steps

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
View the output You'll get info on:

🧾 Certificate validity

🔐 Self-signed or trusted cert

❌ Missing HSTS header

📅 Certificate expiration

🧬 Presence of Subject Alternative Names (SANs)

💣 Detection of LUCKY13 (if possible)

🎥 Demo
Wanna see it in action? Watch the walkthrough on Loom:
👉 Click to watch

🧪 Sample Output
bash
Copy
Edit
[+] Certificate is NOT self-signed ✅  
[+] HSTS header is missing ⚠️  
[+] Certificate will expire in 120 days  
[+] SANs include: www.example.com, example.com  
yaml
Copy
Edit

---

### ✅ 5. Scroll down and commit changes
- At the bottom, you’ll see:
  - A field for **commit message** → write something like: `Added usage steps and demo video`
  - Click ✅ **Commit changes**

---

Boom 💥 your README is now updated with all the info anyone needs to run your project like a pro.

Need help adding screenshots or badges next? I can help you flex that README even more 😎






You said:
i mean inclube open wsl and install testssl.shh and scan website using ./testssl.sh --fast --nodns min https://192.168.56.1:8443 command 


ChatGPT said:
Ahhh gotcha now, Vishnu! 💡 You're saying your project uses WSL and testssl.sh to scan websites, and you wanna include those setup steps in the README.md, right?

No worries, I gotchu 😎 — here's an updated Steps section you can directly copy-paste into your README.md, including WSL, installing testssl.sh, and running the scan:

markdown
Copy
Edit
## ⚙️ Steps to Run with testssl.sh (on WSL)

> 🛡️ This project uses [`testssl.sh`](https://github.com/drwetter/testssl.sh) to scan for SSL/TLS misconfigurations. You can run this from **WSL (Windows Subsystem for Linux)**.

---

### 🧰 Prerequisites

- Windows 10/11 with **WSL installed**
- WSL distro (e.g., Ubuntu)
- Git installed in WSL

---

### 🧪 Setup Instructions

1. **Open WSL**  
   (You can search "Ubuntu" in the Start menu)

2. **Install git (if not already)**
   ```bash
   sudo apt update
   sudo apt install git
Clone testssl.sh repo

bash
Copy
Edit
git clone --depth 1 https://github.com/drwetter/testssl.sh.git
cd testssl.sh
chmod +x testssl.sh
Run the scan Replace https://192.168.56.1:8443 with your target domain/IP.

bash
Copy
Edit
./testssl.sh --fast --nodns https://192.168.56.1:8443
This will:

Skip reverse DNS lookups (--nodns)

Do a quicker scan (--fast)

Show SSL/TLS vulnerabilities and config issues

🧪 Sample Output (Short)
bash
Copy
Edit
 Start 2025-04-21 10:00:00      -->>  https://192.168.56.1:8443 <<--

 Testing protocols via sockets except NPN+ALPN                         via openssl s_client 
 TLS extensions (server name, signature algo,...)                     via openssl s_client 
 Server certificate and hostname matching                            via openssl s_client 
...
 Done 2025-04-21 10:00:45 [  45s] -->>  https://192.168.56.1:8443 <<--
🎥 Demo
Need a walkthrough? Check out the video:
👉 Loom Demo Video

📝 Notes
testssl.sh does not require installation, just clone and run.

Use --jsonfile or --htmlfile options to export reports.

For full scan, remove --fast and --nodns.


