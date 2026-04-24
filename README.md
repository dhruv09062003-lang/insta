Instagram Collaboration Checker (System-Spoiler Edition)

A simple Python-based tool to scan public Instagram profiles and detect tagged collaborators from recent posts using Instagram’s web API.

🚀 Features
🔍 Scan any Instagram username
📊 Displays:
Account status (Public/Private)
Total detected posts
🤝 Extracts tagged users (used as collaboration indicators)
🎨 Colorful CLI interface (with colorama)
⚡ Fast and lightweight
🛠️ Requirements
Python 3.x
Required libraries:
pip install requests colorama

⚠️ If colorama is not installed, the script will still work (without colors).

📦 Installation
git clone https://github.com/yourusername/instagram-collab-checker.git
cd instagram-collab-checker
pip install -r requirements.txt
▶️ Usage
🔹 Run with username as argument:
python3 checker.py username

Example:

python3 checker.py instagram
🔹 Interactive mode:
python3 checker.py

Then enter usernames:

👤 Target Username: nasa

Type exit, quit, or q to close.

📊 Output Example
📊 RESULTS FOR @USERNAME
Status: 🔓 Public
Posts:  10 detected
─────────────────────────────

📌 POST 1
🔗 https://instagram.com/p/XXXXX
🤝 Tagged/Collabs: @user1, @user2

📌 POST 2
🔗 https://instagram.com/p/YYYYY
🤝 No tagged collaborators found.
