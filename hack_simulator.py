import random
import time
import sys

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def random_hex():
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(8))

def simulate_hacking():
    systems = ['MAINFRAME', 'SECURITY', 'NETWORK', 'DATABASE', 'FIREWALL']
    actions = ['Bypassing', 'Infiltrating', 'Decrypting', 'Accessing', 'Breaking']
    
    typing_effect("\n=== SYSTEM BREACH INITIATED ===\n", 0.1)
    time.sleep(1)
    
    # Initial scanning phase
    typing_effect("Scanning for vulnerabilities...", 0.05)
    for _ in range(3):
        time.sleep(0.5)
        print(f"[{random_hex()}] Scanning port {random.randint(1, 9999)}")
    
    # Main "hacking" loop
    attempts = 0
    while True:
        print("\nEnter access code:")
        password = input("> ").lower()
        
        if password == "chair":
            break
        
        attempts += 1
        typing_effect("Access denied!", 0.1)
        time.sleep(0.5)
        
        # Random "hacking" messages
        system = random.choice(systems)
        action = random.choice(actions)
        typing_effect(f"\n{action} {system}...", 0.05)
        for _ in range(2):
            time.sleep(0.3)
            print(f"[{random_hex()}] {random.randint(10, 99)}% complete")
    
    # Success sequence
    typing_effect("\n=== ACCESS GRANTED ===", 0.1)
    time.sleep(1)
    
    for i in range(5):
        typing_effect(f"Downloading data packet {i+1}/5: [{random_hex()}]", 0.05)
        time.sleep(0.3)
    
    typing_effect("\nDownload complete!", 0.1)
    time.sleep(0.5)
    typing_effect("\n=== PROGRAM TERMINATED ===", 0.1)

if __name__ == "__main__":
    simulate_hacking()