def check_balance(balance):
    return f"Your current balance is ₹{balance}"

def deposit_money(balance):
    deposit = int(input("Enter amount to deposit: "))
    balance += deposit
    return f"₹{deposit} has been successfully deposited", balance

def withdraw_money(balance):
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw > balance:
        return "Not enough money", balance
    else:
        balance -= withdraw
        return f"₹{withdraw} has been successfully withdrawn", balance

print("----- ATM Menu -----")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
print("---------------------")

balance = 0

while True:
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(check_balance(balance))
    elif choice == "2":
        msg, balance = deposit_money(balance)
        print(msg)
    elif choice == "3":
        msg, balance = withdraw_money(balance)
        print(msg)
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Enter a valid choice.")
