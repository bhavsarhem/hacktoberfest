import csv
import os
from datetime import datetime

# Initialize an empty list to store expenses
expenses = []
monthly_budget = 0.0

# Function to add an expense
def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter a brief description: ")

    # Create an expense entry
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }

    # Add to the expenses list
    expenses.append(expense)
    print("Expense added successfully!")

# Function to view expenses
def view_expenses():
    if not expenses:
        print("No expenses to display.")
        return

    print("\n--- Expenses ---")
    for expense in expenses:
        date = expense.get('date')
        category = expense.get('category')
        amount = expense.get('amount')
        description = expense.get('description')
        
        if not all([date, category, amount, description]):
            print("Incomplete expense entry, skipping...")
            continue
        
        print(f"Date: {date}, Category: {category}, Amount: {amount}, Description: {description}")
    print("----------------\n")

# Function to set and track the budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    print(f"Monthly budget set to: {monthly_budget}")

def track_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    remaining_balance = monthly_budget - total_expenses

    print(f"\nTotal expenses so far: {total_expenses}")
    if total_expenses > monthly_budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have {remaining_balance} left for the month.\n")

# Function to save expenses to a CSV file
def save_expenses():
    with open('expenses.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for expense in expenses:
            writer.writerow([expense['date'], expense['category'], expense['amount'], expense['description']])
    print("Expenses saved successfully!")

# Function to load expenses from a CSV file
def load_expenses():
    if not os.path.exists('expenses.csv'):
        return

    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense = {
                'date': row['Date'],
                'category': row['Category'],
                'amount': float(row['Amount']),
                'description': row['Description']
            }
            expenses.append(expense)
    print("Expenses loaded successfully!")

# Function to display the menu
def menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if monthly_budget == 0.0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Load existing expenses from the file on program start
load_expenses()
# Display the menu
menu()
