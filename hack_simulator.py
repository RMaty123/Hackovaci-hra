import random
import time
import sys
import string

def typing_effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def random_hex(length=8):
    return ''.join(random.choice('0123456789ABCDEF') for _ in range(length))

def random_ip():
    return f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"

def random_data_stream():
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(random.randint(50, 100)))

def show_menu():
    while True:
        typing_effect("\n=== SYSTEM CONTROL PANEL ===", 0.05)
        print("\n1. Network Scan")
        print("2. Data Extraction")
        print("3. System Analysis")
        print("4. Security Override")
        print("5. Exit")
        
        choice = input("\nSelect operation: ")
        
        if choice == "5":
            typing_effect("\nInitiating shutdown sequence...", 0.05)
            time.sleep(1)
            return
            
        operations = {
            "1": ("Network scanning in progress...", "Found vulnerable nodes"),
            "2": ("Extracting sensitive data...", "Data extraction complete"),
            "3": ("Analyzing system architecture...", "System analysis finished"),
            "4": ("Overriding security protocols...", "Security override successful")
        }
        
        if choice in operations:
            start_msg, end_msg = operations[choice]
            typing_effect(f"\n{start_msg}", 0.05)
            
            # Show random technical-looking output
            for _ in range(random.randint(8, 15)):
                time.sleep(0.2)
                output_type = random.choice([
                    f"[{random_hex()}] Accessing node {random_ip()}",
                    f"[{random_hex()}] {random_data_stream()}",
                    f"[{random_hex()}] Memory block {random_hex(4)}: {random_data_stream()[:30]}",
                    f"[{random_hex()}] Protocol {random.randint(1,9999)} initialized",
                    f"[{random_hex()}] Encryption layer {random.randint(1,16)} bypassed"
                ])
                print(output_type)
            
            typing_effect(f"\n{end_msg}", 0.05)
            time.sleep(1)

def simulate_hacking():
    systems = ['MAINFRAME', 'SECURITY', 'NETWORK', 'DATABASE', 'FIREWALL', 'KERNEL', 'ENCRYPTION', 'AUTHENTICATION']
    actions = ['Bypassing', 'Infiltrating', 'Decrypting', 'Accessing', 'Breaking', 'Exploiting', 'Overriding']
    
    typing_effect("\n=== ADVANCED SYSTEM BREACH INITIATED ===\n", 0.1)
    time.sleep(1)
    
    # Initial scanning phase with more output
    typing_effect("Initiating comprehensive system scan...", 0.05)
    for _ in range(random.randint(5, 8)):
        time.sleep(0.3)
        scan_type = random.choice([
            f"[{random_hex()}] Scanning port {random.randint(1, 9999)}",
            f"[{random_hex()}] Probing {random.choice(systems).lower()} at {random_ip()}",
            f"[{random_hex()}] Analyzing security layer {random.randint(1, 9)}",
            f"[{random_hex()}] {random_data_stream()}"
        ])
        print(scan_type)
    
    # Main "hacking" loop with enhanced feedback
    attempts = 0
    while True:
        print("\nEnter access code:")
        password = input("> ").lower()
        
        if password == "chair":
            break
        
        attempts += 1
        typing_effect("Access denied! Security protocol enhanced.", 0.1)
        time.sleep(0.5)
        
        # Enhanced random "hacking" messages
        for _ in range(random.randint(3, 5)):
            system = random.choice(systems)
            action = random.choice(actions)
            typing_effect(f"\n{action} {system}...", 0.05)
            for _ in range(2):
                time.sleep(0.2)
                print(f"[{random_hex()}] {random_data_stream()}")
                print(f"[{random_hex()}] Progress: {random.randint(10, 99)}%")
    
    # Enhanced success sequence
    typing_effect("\n=== ACCESS GRANTED - SECURITY BYPASSED ===", 0.1)
    time.sleep(1)
    
    typing_effect("\nInitializing system override...", 0.05)
    for i in range(5):
        typing_effect(f"Downloading security package {i+1}/5: [{random_hex()}]", 0.05)
        time.sleep(0.2)
        print(f"[{random_hex()}] {random_data_stream()}")
    
    typing_effect("\nSystem access established!", 0.1)
    time.sleep(0.5)
    
    # Show menu after successful login
    show_menu()
    
    typing_effect("\n=== PROGRAM TERMINATED ===", 0.1)

if __name__ == "__main__":
    simulate_hacking()