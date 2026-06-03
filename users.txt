import os

USER_FILE = "users.txt"

def load_users():
    """Reads users from the text file into a dictionary {username: password}."""
    users = {}
    if not os.path.exists(USER_FILE):
        return users
    try:
        with open(USER_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    users[parts[0]] = parts[1]
    except IOError:
        print("\n[Error] Could not read user credentials file.")
    return users

def register_user():
    """Registers a new user while preventing duplicate usernames."""
    print("\n--- User Registration ---")
    users = load_users()
    
    username = input("Create Username: ").strip()
    if not username:
        print("[Error] Username cannot be empty.")
        return False
        
    if username in users:
        print("[Error] Username already exists. Please choose another one.")
        return False
        
    password = input("Create Password: ").strip()
    if not password:
        print("[Error] Password cannot be empty.")
        return False

    try:
        with open(USER_FILE, "a") as file:
            file.write(f"{username},{password}\n")
        print(f"\n[Success] Account for '{username}' created successfully!")
        return True
    except IOError:
        print("\n[Error] Failed to save user credentials.")
        return False

def login_user():
    """Validates user credentials for logging into the system."""
    print("\n--- User Login ---")
    users = load_users()
    
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if username in users and users[username] == password:
        print(f"\n[Success] Welcome back, {username}!")
        return True
    else:
        print("\n[Error] Invalid username or password.")
        return False
