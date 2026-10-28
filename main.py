
#expense tracker project

expenses=[] #list of all expenses
print("Welcome to Expense Tracker : Spend less")

while True:
    print("===MENU===")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Spending")
    print("4.Exit")

    choice=input("Please Enter your choice : ")

    #ADD EXPENSES

    if (choice == "1"):
        date=input("Enter the date: ")
        category=input("Enter the category: ")
        description=input("More details: ")
        amount=float(input("Enter the amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\n expense is added successfully")

    #2.view all expenses

    elif(choice == "2"):
        if(len(expenses)==0):
            print("no expenses added")
        else:
            print("===your all expenses===")
            count=1
            for eachexpenses in expenses:
                print(f"expenses no {count} -> {eachexpenses['date']}, {eachexpenses['category']}, {eachexpenses['description']}, {eachexpenses['amount']}")
                count=count+1

    #3.view total spending

    elif(choice == "3"):
        total=0
        for eachexpenses in expenses:
            total=total+eachexpenses["amount"]
        print("\nTotal expenses= ",total)

    #4.exit

    elif(choice == "4"):
        print("Thank you for using our system")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
