import time
import datetime
import os

# Tokyo Night-inspired ANSI color codes
RESET   = "\033[0m"
CYAN    = "\033[96m"
BLUE    = "\033[94m"
MAGENTA = "\033[95m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
BOLD    = "\033[1m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(prompt, cast_type=str):
    while True:
        try:
            return cast_type(input(CYAN + prompt + GREEN))
        except:
            print(RED + "Invalid input. Try again." + RESET)

def print_coin_feedback(coin_count):
    print(f"\n{YELLOW}{BOLD}💰 +1 START COIN! 💥{RESET}")
    print(YELLOW + r"""
     _______
    /       \
   |  START  |
    \_______/
    
    """ + RESET)
    print(f"{GREEN}Total Start Coins: {coin_count}{RESET}")
    print(BLUE + "-" * 30 + RESET)

def main():
    clear()
    print(MAGENTA + "=== SESSION START ===" + RESET)
    bank_balance = get_input("Enter your current bank balance: $", float)

    start_time_raw = time.time()
    start_time_str = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\n🎬 {YELLOW}Session started at {start_time_str}{RESET}")
    print(f"{CYAN}Press ENTER to collect a START COIN.")
    print(RESET + "Type 'pause' to pause, 'resume' to resume, 'end' to finish the session.\n" + RESET)

    paused = False
    pause_start = 0
    total_paused = 0
    start_coins = 0

    while True:
        cmd = input(">> ").strip().lower()
        if cmd == "":
            start_coins += 1
            print_coin_feedback(start_coins)
        elif cmd == "pause":
            if not paused:
                pause_start = time.time()
                paused = True
                print(MAGENTA + "⏸️  Session paused." + RESET)
        elif cmd == "resume":
            if paused:
                total_paused += time.time() - pause_start
                paused = False
                print(GREEN + "▶️  Session resumed." + RESET)
        elif cmd == "end":
            break
        else:
            print(RED + "Invalid command. Use ENTER / pause / resume / end" + RESET)

    end_time_raw = time.time()
    end_time_str = datetime.datetime.now().strftime("%H:%M:%S")
    total_duration = int(end_time_raw - start_time_raw - total_paused)
    duration_str = time.strftime('%H:%M:%S', time.gmtime(total_duration))

    print(MAGENTA + "\n=== SESSION END ===" + RESET)
    animations_done = get_input("Animations finished: ", int)
    animations_left = get_input("Animations still to do: ", int)
    animations_in_progress = get_input("Animations in progress (started, not finished): ", int)

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"session_{timestamp}.txt"

    with open(filename, 'w') as f:
        f.write("Session Summary\n")
        f.write("--------------------\n")
        f.write(f"Start Time: {start_time_str}\n")
        f.write(f"End Time: {end_time_str}\n")
        f.write(f"Duration: {duration_str}\n")
        f.write(f"Start Coins: {start_coins}\n\n")
        f.write(f"Bank Balance (start): ${bank_balance:.2f}\n")
        f.write(f"Animations Finished: {animations_done}\n")
        f.write(f"Animations In Progress: {animations_in_progress}\n")
        f.write(f"Animations Left: {animations_left}\n\n")
        f.write(f"Date: {now.strftime('%Y-%m-%d')}\n")

    print(f"\n{GREEN}📁 Session saved to: {filename}{RESET}")
    print(BOLD + "🔥 Great job today. Keep the grind alive!" + RESET)

if __name__ == "__main__":
    main()
