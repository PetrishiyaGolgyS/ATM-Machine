print("\t\tWelcome to XXX ATM")
print("------------------------------------------------------")
Balance = 10000

pin = int(input("Enter the pin: "))
if pin == 1234:
    print("PIN accepted")
    while True:
        print("\t ATM Menu")
        
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        option = int(input("Enter your choice: "))
        
        if option == 1:
            print("Your current balance is", Balance)
            print("------------------------------------------------------")
        
        elif option == 2:
            print("Your current balance is", Balance)
            withdraw = int(input("Enter the amount: "))
            if withdraw > Balance:
                print("The entered amount exceeds your current balance")
                print("Try again by entering amount that matches your balance range")
                print("------------------------------------------------------")
            else:
                Balance -= withdraw
                print("Successfully withdrawn", withdraw)
                print("The current balance is", Balance)
                print("------------------------------------------------------")
        
        elif option == 3:
            Deposit = int(input("Enter the amount to be deposited: "))
            Balance += Deposit
            print("Successfully Deposited", Deposit)
            print("The current balance is", Balance)
            print("------------------------------------------------------")
        
        elif option == 4:
            print("Exit.Thankyou for Visiting the ATM")
            break

else:
    print("Invalid PIN")
