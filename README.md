# 📸 Instagram Collaboration Checker  
### ⚡ System-Spoiler Edition

## 🧾 Overview
The Instagram Collaboration Checker is a lightweight command-line Python tool designed to scan Instagram profiles and extract publicly available metadata.

It helps in:
- Quick reconnaissance  
- Social media analysis  
- Detecting collaborations via tagged users  

---

## 🚀 Key Features
- Profile Scanning: Fetches username, privacy status, and post count  
- Collaboration Analysis: Analyzes the latest 5 posts to detect tagged users  
- Adaptive UI: Uses `colorama` for styled output with fallback support  
- Dual Mode Execution:
  - CLI argument mode  
  - Interactive input mode  
- Error Handling:
  - Handles 404 errors  
  - API failures  
  - Timeouts  
  - Restricted/private accounts  

---

## 🛠️ Requirements
- Python Version: 3.6+

### Required Libraries
```bash
pip install requests colorama
```

> colorama is optional (used for colored output)

---

## 📥 Installation
```bash
git clone https://github.com/dhruv09062003-lang/instagram-collab-checker.git
cd instagram-collab-checker
pip install -r requirements.txt
```

---

## ▶️ Usage Instructions

### 1. Run with Username Argument
```bash
python3 insta.py <username>
```

Example:
```bash
python3 insta.py nasa
```

---

### 2. Interactive Mode
```bash
python3 insta.py
```

Then input:
```
👤 Target Username: nasa
```

Type `exit`, `quit`, or `q` to terminate the program.

---

## 📊 Output Example
```
📊 RESULTS FOR @NASA
Status: 🔓 Public
Posts: 10 detected
─────────────────────────────

📌 POST 1
🔗 https://instagram.com/p/XXXXX
🤝 Tagged/Collabs: @user1, @user2

📌 POST 2
🔗 https://instagram.com/p/YYYYY
🤝 No tagged collaborators found.
```

---

## ⚙️ Working Mechanism
1. User Input & Sanitization  
   - Accepts username via CLI or input  
   - Removes '@' and extra spaces  

2. Request Construction  
   - Uses endpoint:
     /api/v1/users/web_profile_info/  
   - Adds headers (App ID, Referer, User-Agent)  

3. JSON Parsing  
   - Extracts post data from:
     edge_owner_to_timeline_media  

4. Collaboration Mapping  
   - Checks:
     edge_media_to_tagged_user  
   - Tagged users are treated as collaborators  

5. Output Generation  
   - Displays profile info, post links, and collaborators  

---

## 🔧 Technical Implementation
- Uses `requests` library  
- Simulates browser headers (no login required)  
- Lightweight alternative to Selenium and official APIs  

---

## ⚠️ Limitations
- Works only on public accounts  
- Instagram may change API endpoints or apply rate limits  
- Collaboration detection is based on tagged users  

---

## 🔐 Cybersecurity Relevance
- OSINT (Open Source Intelligence)  
- Public data extraction  
- Reconnaissance techniques  
- API exposure awareness  

---

## 📌 Disclaimer
This tool is for educational and ethical research purposes only.

- Do not misuse  
- Respect privacy and platform policies  
- Excessive use may result in IP rate-limiting  

---

## 👨‍💻 Author
System-Spoiler

---

## ⭐ Contributing
Pull requests are welcome. Feel free to fork and improve the project.
