import requests
import time
import os
import sys
from colorama import init, Fore, Style

# Initialize Colorama (Fix for Color Codes Not Showing Properly)
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_animated_logo():
    clear_screen()
    logo_lines = [
 
  ("/$$$$$$  /$$     /$$ /$$   /$$  /$$$$$$  /$$   /$$       /$$$$$$$   /$$$$$$     /$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$$", Fore.YELLOW),     
 ("/$$__  $$|  $$   /$$/| $$  | $$ /$$__  $$| $$  | $$      | $$__  $$ /$$__  $$   |__  $$| $$__  $$| $$  | $$|__  $$__/", Fore.YELLOW),      
("| $$  \ $$ \  $$ /$$/ | $$  | $$| $$  \__/| $$  | $$      | $$  \ $$| $$  \ $$      | $$| $$  \ $$| $$  | $$   | $$", Fore.GREEN),        
("| $$$$$$$$  \  $$$$/  | $$  | $$|  $$$$$$ | $$$$$$$$      | $$$$$$$/| $$$$$$$$      | $$| $$$$$$$/| $$  | $$   | $$", Fore.CYAN),     
("| $$__  $$   \  $$/   | $$  | $$ \____  $$| $$__  $$      | $$__  $$| $$__  $$ /$$  | $$| $$____/ | $$  | $$   | $$", Fore.GREEN),        
("| $$  | $$    | $$    | $$  | $$ /$$  \ $$| $$  | $$      | $$  \ $$| $$  | $$| $$  | $$| $$      | $$  | $$   | $$", Fore.GREEN),         
("| $$  | $$    | $$    |  $$$$$$/|  $$$$$$/| $$  | $$      | $$  | $$| $$  | $$|  $$$$$$/| $$      |  $$$$$$/   | $$", Fore.YELLOW),        
("|__/  |__/    |__/     \______/  \______/ |__/  |__/      |__/  |__/|__/  |__/ \______/ |__/       \______/    |__/", Fore.YELLOW),              
("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN),
("         │                         【•】 YOUR COUNTRY  ➤ INDIA                            │", Fore.CYAN),
("         │                         【•】 YOUR REGION   ➤ UP                               │", Fore.CYAN),
("         │                         【•】 YOUR CITY     ➤ BAREILLY                         │", Fore.CYAN),
("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN),
("", Fore.RESET),
("╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.YELLOW),
("║  NAME                 : BROKEN-AYUSH           GOD ABBUS                     RAKHNA               ║", Fore.CYAN),
("║  RULLEX               : UP  ON FIRE            KARNE PE                     SAB GOD               ║", Fore.GREEN),
("║  FORM 🏠              : BIHAR-PATNA              APPEARED                     ABBUS BANA          ║", Fore.CYAN),
("║  BRAND                : MULTI CONVO              HATA DIYA                    HAI BILKUL          ║", Fore.GREEN),
("║  GitHub               : BROKEN AYUSH            JAAEGA YE                    KOI BHI HO           ║", Fore.CYAN),
("║  WHATSAP              : +918287041662            BAAT YWAD                   GOD ABBUS NO         ║", Fore.GREEN),
("╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.YELLOW),
]



    for line, color in logo_lines:
        typing_effect(line, 0.005, color)

    typing_effect("                       <<━━━━━━━━━━━━━━━━━━⏮️⚓BROK3N-AYUSH⚓⏭️━━━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "{<<══════════════════════════════════════BROKEN AYUSH HERE═══════════════════════════════════════>>}")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException:
        exit(1)

def fetch_profile_name(access_token):
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown")
    except requests.exceptions.RequestException:
        return "Unknown"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token})
        response.raise_for_status()
        return response.json().get("name", "Unknown Target")
    except requests.exceptions.RequestException:
        return "Unknown Target"

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = [token.strip() for token in file.readlines()]

    token_profiles = {token: fetch_profile_name(token) for token in tokens}
    target_profile_name = fetch_target_name(target_id, tokens[0])  

    headers = {"User-Agent": "Mozilla/5.0"}

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index]
            sender_name = token_profiles.get(access_token, "Unknown Sender")
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}

            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")

                print(Fore.YELLOW + f"\n<<═══════════════════════BROTHER═════════════AYUSH DONE═════════════NADEEM DONE════════════════════>>")
                typing_effect(f"[🎉] MESSAGE {message_index + 1} SUCCESSFULLY SENT!", 0.02, Fore.CYAN)
                typing_effect(f"[👤] SENDER: {sender_name}", 0.02, Fore.WHITE)
                typing_effect(f"[📩] TARGET: {target_profile_name} ({target_id})", 0.02, Fore.MAGENTA)
                typing_effect(f"[📨] MESSAGE: {full_message}", 0.02, Fore.LIGHTGREEN_EX)
                typing_effect(f"[⏰] TIME: {current_time}", 0.02, Fore.LIGHTWHITE_EX)
                print(Fore.YELLOW + f"<<═══════════════════════BROTHER═════════════AYUSH DONE═════════════NADEEM DONE════════════════════>>\n")

            except requests.exceptions.RequestException:
                continue  

            time.sleep(speed)

        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    clear_screen()
    display_animated_logo()

    pastebin_url = "https://pastebin.com/raw/6kAVm6cm"
    correct_password = fetch_password_from_pastebin(pastebin_url)

    entered_password = animated_input("  【👑】 ENTER OWNER NAME➜")
    tokens_file = animated_input(" 【📕】 ENTER TOKEN FILE➜")
    target_id = animated_input("  【🖇️】  ENTER CONVO UID ➜")
    haters_name = animated_input("  【🖊️】 ENTER HATER NAME➜")
    messages_file = animated_input("  【📝】 ENTER MESSAGE FILE➜")
    speed = float(animated_input("  【⏰】 ENTER DELAY/TIME (in seconds) FOR MESSAGES ➜"))

    if entered_password != correct_password:
        print(Fore.RED + "[x] Incorrect OWNER NAME. Exiting program.")
        exit(1)

    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
