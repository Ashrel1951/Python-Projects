
import json
from datetime import datetime

class Expense:
    
    # Represents an expense with a category, amount, date, and description.
    
    def __init__(self, category, amount, date, description):
        self.category = category
        self.amount = amount
        self.date = date
        self.description = description

    def to_dict(self):
        
        # Converts the Expense object to a dictionary for JSON serialization.
        
        return {
            "category": self.category,
            "amount": self.amount,
            "date": self.date,
            "description": self.description,
        }

class ExpenseTracker:
    
    # Tracks expenses and provides functionality to add, view, save, and load them.
    
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses_from_file()

    def add_expense(self):
        
        # Prompts the user to input expense details and adds it to the tracker.
        
        category = input("Enter category: ")
        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD.")
            return

        description = input("Enter description: ")
        expense = Expense(category, amount, date, description)
        self.expenses.append(expense)
        print("Expense added successfully!")

    def view_expenses(self):
        
        # Displays all expenses in the tracker in a readable format.
        
        if not self.expenses:
            print("No expenses to show.")
            return

        print("\nExpenses:")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp.category} | {exp.amount} | {exp.date} | {exp.description}")

    def save_expenses_to_file(self):
        
        # Saves all expenses to the specified JSON file.
        
        with open(self.filename, 'w') as file:
            json.dump([exp.to_dict() for exp in self.expenses], file)
        print("Expenses saved to file.")

    def load_expenses_from_file(self):
        
        # Loads expenses from the specified JSON file if it exists.
        
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Expense(**item) for item in data]
        except FileNotFoundError:
            return []

    def main_menu(self):
        
        # Displays the main menu and handles user input for various actions.
        
        print("Welcome to the Expense Tracker!")
        while True:
            print("\nMenu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Save and Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.save_expenses_to_file()
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()  # Create an instance of the ExpenseTracker class
    tracker.main_menu()  # Start the main menu
