def add_expense(expense_list,expense):
    expense_list.append(expense)
    return expense
  
def calculate_total(expense_list):
    total = sum(expense_list)
    return total
  
def find_highest_expense(expense_list):
    highest_expense = max(expense_list)
    return highest_expense
  
def convert_expense(expense, conversion_rate):
    converted_expense = expense*conversion_rate
    return converted_expense
  
def main():
  
  expenses = [] 
  
  while True:
    user_input = input("enter an expense amount(or type 'done' to finish): ")
    if user_input.lower() == 'done':
      break
    try:
      expense = float(user_input)
      print(add_expense(expenses, expense))
      
    except ValueError:
      print("invalid input. please enter a valid number")
      
      
  if expenses:
    
    print (f"/n your expenses: {expenses}")
    
    total_expense = calculate_total(expenses)
    print(f"total expense: ${total_expense}")
    
    highest_expense = find_highest_expense(expenses)
    print(f"Highest expense: ${highest_expense:.2f}")

    # Asking if the user wants to convert the total expense
    conversion_choice = input("Do you want to convert the total expense to another currency? (yes/no): ").lower()
    if conversion_choice == 'yes':
        conversion_rate = float(input("Enter the conversion rate (e.g., 0.85 for USD to EUR): "))
        converted = convert_expense(total_expense, conversion_rate)
        print(f"Total expense in converted currency: {converted:.2f}")
    else:
     print("No expenses were entered.")

    
    
    
      
  
main()