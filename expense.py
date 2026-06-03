mport os

DATA_FILE = "budget_data.txt"

def load_data():
    """Loads transactions from the text file into a list of dictionaries."""
    transactions = []
    if not os.path.exists(DATA_FILE):
        return transactions
    
    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    transactions.append({
                        "id": parts[0],
                        "category": parts[1],
                        "type": parts[2],
                        "amount": float(parts[3]),
                        "date": parts[4]
                    })
    except (IOError, ValueError):
        print("\n[Error] Could not read or parse the data file properly.")
    return transactions

def save_data(transactions):
    """Saves the list of dictionaries back to the text file."""
    try:
        with open(DATA_FILE, "w") as file:
            for t in transactions:
                file.write(f"{t['id']},{t['category']},{t['type']},{t['amount']},{t['date']}\n")
    except IOError:
        print("\n[Error] Failed to save changes to the file.")

def create_transaction(category, trans_type, amount, date):
    """CREATE: Adds a new transaction entry."""
    transactions = load_data()
    
    if transactions:
        new_id = str(max(int(t['id']) for t in transactions) + 1)
    else:
        new_id = "1"
        
    new_transaction = {
        "id": new_id,
        "category": category,
        "type": trans_type,
        "amount": amount,
        "date": date
    }
    
    transactions.append(new_transaction)
    save_data(transactions)
    print(f"\n[Success] Transaction ID {new_id} added successfully!")

def update_transaction(trans_id, new_category, new_type, new_amount, new_date):
    """UPDATE: Modifies an existing transaction profile."""
    transactions = load_data()
    found = False
    
    for t in transactions:
        if t['id'] == trans_id:
            t['category'] = new_category
            t['type'] = new_type
            t['amount'] = new_amount
            t['date'] = new_date
            found = True
            break
            
    if found:
        save_data(transactions)
        print(f"\n[Success] Transaction ID {trans_id} updated successfully!")
    else:
        print(f"\n[Error] Transaction ID {trans_id} not found.")

def delete_transaction(trans_id):
    """DELETE: Removes a transaction from the record."""
    transactions = load_data()
    initial_length = len(transactions)
    
    transactions = [t for t in transactions if t['id'] != trans_id]
    
    if len(transactions) < initial_length:
        save_data(transactions)
        print(f"\n[Success] Transaction ID {trans_id} deleted successfully!")
    else:
        print(f"\n[Error] Transaction ID {trans_id} not found.")
