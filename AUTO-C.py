import os
import subprocess
import time
import sys
import struct
from itertools import cycle

# Colors for terminal text (ANSI escape codes)
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']  # Removed reset code
RESET = '\033[0m'

def colorful_loading_animation(duration=20):
    end_time = time.time() + duration
    symbols = ['|', '/', '-', '\\']
    color_cycle = cycle(COLORS)

    while time.time() < end_time:
        for symbol in symbols:
            color = next(color_cycle)
            os.system('clear')
            sys.stdout.write(f'\r{color}Loading... {symbol}{RESET}')
            sys.stdout.flush()
            time.sleep(0.25)
    sys.stdout.write(f'\r\033[92mLoading complete! {RESET}\n')

def open_whatsapp_link():
    link = "https://chat.whatsapp.com/FxmYo9dizXg2I1XbDkEfmi"
    try:
        if os.name == 'nt':
            subprocess.run(["start", link], shell=True)
        elif os.name == 'posix':
            subprocess.run(["xdg-open", link])
    except Exception as e:
        print(f"{RESET}\033[91mFailed to open WhatsApp link: {e}{RESET}")

def check_64bit():
    if struct.calcsize("P") * 8 != 64:
        print(f"\033[91mThis tool requires a 64-bit system!{RESET}")
        sys.exit(1)

def main():
    try:
        colorful_loading_animation()
        check_64bit()
        open_whatsapp_link()

        try:
            import AUTCC
            if hasattr(AUTCC, 'menu'):
                print(f"{RESET}▶️ Running menu function...")
                AUTCC.menu()  # Changed from main() to menu()
            else:
                print(f"{RESET}\033[93m'menu' function not found in AUTCC module{RESET}")
                print("Available functions:", [f for f in dir(AUTCC) if not f.startswith('_')])
        except ImportError as e:
            print(f"{RESET}\033[91mAUTCC module not found: {e}{RESET}")

    except Exception as e:
        print(f"{RESET}\033[91mUnexpected error: {e}{RESET}")

if __name__ == "__main__":
    main()
