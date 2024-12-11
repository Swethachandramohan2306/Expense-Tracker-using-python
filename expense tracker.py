class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        name = input("Enter the name of the expense: ")
        amount = float(input("Enter the amount spent: "))
        date = input("Enter the date of expense (DD/MM/YYYY): ")

        expense = {
            "name": name,
            "amount": amount,
            "date": date
        }
        self.expenses.append(expense)
        print("Expense added successfully!\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses to show.\n")
            return

        print("\nYour expenses:")
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. {expense['name']} - ${expense['amount']} on {expense['date']}")

    def delete_expense(self):
        self.view_expenses()
        if not self.expenses:
            return

        try:
            expense_index = int(input("\nEnter the expense number to delete: ")) - 1
            if 0 <= expense_index < len(self.expenses):
                deleted_expense = self.expenses.pop(expense_index)
                print(f"Deleted expense: {deleted_expense['name']} - ${deleted_expense['amount']} on {deleted_expense['date']}\n")
            else:
                print("Invalid expense number.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    def show_total_expenses(self):
        if not self.expenses:
            print("No expenses recorded.\n")
            return

        total = sum(expense["amount"] for expense in self.expenses)
        print(f"Total expenses: ${total:.2f}\n")

def main():
    tracker = ExpenseTracker()
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.delete_expense()
        elif choice == '4':
            tracker.show_total_expenses()
        elif choice == '5':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()
