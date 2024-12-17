def add_expense(expenses):
    name = input("Enter the name of the expense: ")
    amount = float(input("Enter the amount spent: "))
    date = input("Enter the date of expense (DD/MM/YYYY): ")

    expense = {
        "name": name,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.\n")
        return

    print("\nYour expenses:")
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ${expense['amount']} on {expense['date']}")

def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return

    try:
        expense_index = int(input("\nEnter the expense number to delete: ")) - 1
        if 0 <= expense_index < len(expenses):
            deleted_expense = expenses.pop(expense_index)
            print(f"Deleted expense: {deleted_expense['name']} - ${deleted_expense['amount']} on {deleted_expense['date']}\n")
        else:
            print("Invalid expense number.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def show_total_expenses(expenses):
    if not expenses:
        print("No expenses recorded.\n")
        return

    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ${total:.2f}\n")

def main():
    expenses = []
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Show Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            delete_expense(expenses)
        elif choice == '4':
            show_total_expenses(expenses)
        elif choice == '5':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please choose again.\n")

if __name__ == "__main__":
    main()
