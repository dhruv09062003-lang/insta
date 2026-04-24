#!/usr/bin/env python3
"""
Instagram Collaboration Checker - System-Spoiler Edition
"""

import requests
import sys
import os

# Try to import colorama for styling; fall back to plain text if not installed
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    # Mock classes to prevent errors if colorama is missing
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = Back = Style = MockColor()

def print_banner():
    """Displays the System-Spoiler header"""
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
    {Fore.CYAN}╔════════════════════════════════════════════╗
    {Fore.CYAN}║{Fore.YELLOW}           SYSTEM-SPOILER PRESENT          {Fore.CYAN}║
    {Fore.CYAN}║{Fore.WHITE}       Instagram Collaboration Checker      {Fore.CYAN}║
    {Fore.CYAN}╚════════════════════════════════════════════╝
    """
    print(banner)

def get_instagram_data(username):
    """Get Instagram collaboration data"""
    print(f"{Fore.BLUE}🔍 Scanning @{username}...")
    
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "X-IG-App-ID": "936619743392459",
        "Referer": f"https://www.instagram.com/{username}/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        
        if response.status_code == 404:
            print(f"{Fore.RED}❌ User not found")
            return
        elif response.status_code != 200:
            print(f"{Fore.RED}❌ Error {response.status_code}: Check your connection or IG API status.")
            return
        
        data = response.json()
        user = data["data"]["user"]
        
        if not user:
            print(f"{Fore.RED}❌ Could not retrieve user data.")
            return

        username = user.get("username", "Unknown")
        is_private = user.get("is_private", False)
        profile_type = f"{Fore.RED}🔒 Private" if is_private else f"{Fore.GREEN}🔓 Public"
        
        posts = user.get("edge_owner_to_timeline_media", {}).get("edges", [])
        
        print(f"\n{Fore.MAGENTA}📊 RESULTS FOR @{username.upper()}")
        print(f"Status: {profile_type}")
        print(f"Posts:  {Fore.CYAN}{len(posts)} detected")
        print(f"{Fore.CYAN}" + "─" * 45)
        
        if not posts:
            print(f"{Fore.YELLOW}No posts found or account is restricted.")
            return
        
        for i, post in enumerate(posts[:5], 1):
            node = post["node"]
            shortcode = node["shortcode"]
            
            print(f"\n{Fore.YELLOW}📌 POST {i}")
            print(f"{Fore.WHITE}🔗 https://instagram.com/p/{shortcode}")
            
            # Instagram's web API often hides collab details in the summary 
            # Check tagged users as a proxy for collaborators
            tagged = node.get("edge_media_to_tagged_user", {}).get("edges", [])
            
            if tagged:
                collab_list = [f"{Fore.GREEN}@{u['node']['user']['username']}" for u in tagged]
                print(f"{Fore.WHITE}🤝 Tagged/Collabs: {', '.join(collab_list)}")
            else:
                print(f"{Fore.WHITE}🤝 No tagged collaborators found.")
        
        print(f"\n{Fore.CYAN}" + "─" * 45)
        
    except Exception as e:
        print(f"{Fore.RED}❌ System Error: {str(e)}")

def main():
    """Main execution loop"""
    print_banner()
    
    if len(sys.argv) > 1:
        username = sys.argv[1].replace("@", "")
        get_instagram_data(username)
    else:
        print(f"{Fore.WHITE}Type {Fore.RED}'exit'{Fore.WHITE} to close the program.")
        
        while True:
            try:
                username = input(f"\n{Fore.GREEN}👤 Target Username: {Fore.WHITE}").strip()
                
                if username.lower() in ['quit', 'exit', 'q']:
                    print(f"{Fore.YELLOW}Shutting down... Goodbye!")
                    break
                
                if not username:
                    continue
                
                get_instagram_data(username.replace("@", ""))
                
            except KeyboardInterrupt:
                print(f"\n{Fore.YELLOW}Session ended.")
                break

if __name__ == "__main__":
    main()
