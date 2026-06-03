import users
import expense
import report

def budget_menu():
    """The core menu-driven loop for managing the budget system."""
    while True:
        print("\n*** BUDGET TRACKER SYSTEM *")
        print("[1] Add Transaction (Create)")
        print("[2] View Transactions (Read)")
        print("[3] Update Transaction (Update)")
        print("[4] Delete Transaction (Delete)")
        print("[5] Log Out")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            print("\n--- Add New Transaction ---")
            category = input("Enter Category (e.g., Food, Salary, Rent): ").strip()
            
            while True:
                trans_type = input("Enter Type (Income / Expense): ").strip().upper()
                if trans_type in ["INCOME", "EXPENSE"]:
                    break
                print("[Invalid Input] Please type exactly 'Income' or 'Expense'.")
            
            while True:
                try:
                    amount = float(input("Enter Amount: "))
                    if amount <= 0:
                        print("[Invalid Input] Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("[Invalid Input] Please enter a valid numerical value.")
                    
            date = input("Enter Date (YYYY-MM-DD): ").strip()
            expense.create_transaction(category, trans_type, amount, date)
            
        elif choice == '2':
            report.view_transactions()
            
        elif choice == '3':
            print("\n--- Update Existing Transaction ---")
            trans_id = input("Enter the Transaction ID to update: ").strip()
            category = input("Enter New Category: ").strip()
            
            while True:
                trans_type = input("Enter New Type (Income / Expense): ").strip().upper()
                if trans_type in ["INCOME", "EXPENSE"]:
                    break
                print("[Invalid Input] Please type exactly 'Income' or 'Expense'.")
                
            while True:
                try:
                    amount = float(input("Enter New Amount: "))
                    if amount <= 0:
                        print("[Invalid Input] Amount must be greater than 0.")
                        continue
                    break
                except ValueError:
                    print("[Invalid Input] Please enter a valid numerical value.")
                    
            date = input("Enter New Date (YYYY-MM-DD): ").strip()
            expense.update_transaction(trans_id, category, trans_type, amount, date)
            
        elif choice == '4':
            print("\n--- Delete Transaction ---")
            trans_id = input("Enter the Transaction ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete transaction ID {trans_id}? (YES/NO): ").strip().upper()
            if confirm == "YES":
                expense.delete_transaction(trans_id)
            else:
                print("\nDeletion canceled.")
                
        elif choice == '5':
            print("\nLogging out of budget profile...")
            break
        else:
            print("\n[Invalid Selection] Please choose a valid option from 1 to 5.")

def main():
    """Gatekeeper loop handling Authentication before system access."""
    while True:
        print("\n======================================")
        print("  WELCOME TO BUDGET TRACKER SYSTEM   ")
        print("======================================")
        print("[1] Register New Account")
        print("[2] Log In")
        print("[3] Exit Application")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == '1':
            users.register_user()
        elif choice == '2':
            if users.login_user():
                budget_menu()
        elif choice == '3':
            print("\nGoodbye! Thank you for using our software.")
            break
        else:
            print("\n[Invalid Selection] Please choose 1, 2, or 3.")

if _name_ == "_main_":
    main()
