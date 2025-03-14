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

def random_bank_account():
    return ''.join(random.choice('0123456789') for _ in range(16))

def hack_bank_account():
    typing_effect("\n=== BANK ACCOUNT BREACH INITIATED ===", 0.05)
    
    source_account = random_bank_account()
    target_account = random_bank_account()
    amount = random.randint(10000, 999999)
    
    typing_effect(f"\nTarget Account Found: {source_account}", 0.05)
    typing_effect(f"Available Balance: ${amount:,}", 0.05)
    typing_effect(f"\nTransfer to Account: {target_account}", 0.05)
    
    confirm = input("\nProceed with transfer? (yes/no): ").lower()
    
    if confirm == 'yes':
        typing_effect("\nInitiating secure transfer protocol...", 0.05)
        
        for i in range(5):
            progress = random.randint(1, 100)
            typing_effect(f"Transfer progress: {progress}%", 0.02)
            print(f"[{random_hex()}] Encrypting transaction data...")
            print(f"[{random_hex()}] Routing through proxy {random_ip()}")
            time.sleep(0.3)
        
        typing_effect(f"\nSuccessfully transferred ${amount:,}", 0.05)
        typing_effect("Transaction complete. Covering tracks...", 0.05)
        time.sleep(1)
    else:
        typing_effect("\nTransfer aborted. Clearing traces...", 0.05)

def show_menu():
    while True:
        typing_effect("\n=== SYSTEM CONTROL PANEL ===", 0.05)
        print("\n1. Network Scan")
        print("2. Data Extraction")
        print("3. System Analysis")
        print("4. Security Override")
        print("5. Bank Account Hack")
        print("6. Exit")
        
        choice = input("\nSelect operation: ")
        
        if choice == "6":
            typing_effect("\nInitiating shutdown sequence...", 0.05)
            time.sleep(1)
            return
            
        if choice == "5":
            hack_bank_account()
            continue
            
        operations = {
            "1": ("Network scanning in progress...", "Found vulnerable nodes"),
            "2": ("Extracting sensitive data...", "Data extraction complete"),
            "3": ("Analyzing system architecture...", "System analysis finished"),
            "4": ("Overriding security protocols...", "Security override successful")
        }
        
        if choice in operations:
            start_msg, end_msg = operations[choice]
            typing_effect(f"\n{start_msg}", 0.05)
            
            # Enhanced network scan results
            if choice == "1":
                vulnerable_ports = [21, 22, 23, 25, 53, 80, 443, 3306, 5432]
                for _ in range(random.randint(5, 10)):
                    ip = random_ip()
                    port = random.choice(vulnerable_ports)
                    status = random.choice(["VULNERABLE", "OPEN", "UNSECURED"])
                    service = random.choice(["FTP", "SSH", "TELNET", "SMTP", "DNS", "HTTP", "HTTPS", "MySQL", "PostgreSQL"])
                    print(f"[{random_hex()}] {ip}:{port} - {status} - {service}")
                    time.sleep(0.2)
            else:
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
    typing_effect("\n=== ADVANCED SYSTEM BREACH INITIATED ===\n", 0.1)
    time.sleep(1)
    
    while True:
        print("\nEnter access code:")
        password = input("> ").lower()
        
        if password == "chair":
            break
        
        typing_effect("Access denied!", 0.1)
    
    # Quick success sequence
    typing_effect("\n=== ACCESS GRANTED - SECURITY BYPASSED ===", 0.1)
    time.sleep(0.5)
    
    # Show menu after successful login
    show_menu()
    
    typing_effect("\n=== PROGRAM TERMINATED ===", 0.1)

if __name__ == "__main__":
    simulate_hacking()