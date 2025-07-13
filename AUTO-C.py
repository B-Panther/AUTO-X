import os
import subprocess
import time
import sys
from itertools import cycle

# Colors for terminal text (ANSI escape codes)
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']  # Removed reset code
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
        if os.name == 'nt':  # Windows
            subprocess.run(["start", link], shell=True)
        elif os.name == 'posix':  # macOS/Linux
            subprocess.run(["xdg-open", link])
    except Exception as e:
        print(f"⚠️ Failed to open link: {e}")

def main():
    try:
        colorful_loading_animation()
        print("\033[93mThis tool is only for 64-bit systems!\033[0m")
        open_whatsapp_link()

        # Check if AUTCC exists and has main() function
        try:
            import AUTCC
            if hasattr(AUTCC, 'main'):
                print("▶️ Running main function...")
                AUTCC.main()
            else:
                print("⚠️ 'main' function not found in AUTCC module")
                print("Available functions:", [func for func in dir(AUTCC) if not func.startswith('_')])
        except ImportError:
            print("❌ AUTCC module not found")
            print("Please ensure AUTCC.py exists in your directory")

    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
