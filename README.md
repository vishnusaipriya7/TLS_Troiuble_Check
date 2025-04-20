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



