choice = int(input('''Please choose what you want to do from the list below
                          1. Addition         2. Subtraction
                          3. Multiplication   4. Division
                          5. Exponentiation 
                          ENTER YOUR CHOICE HERE  '''))
#Addition module
if choice == 1:
    x = int(input("Enter number 1 "))
    y = int(input("Enter number 1 "))
    z = x + y

    print(f"The summation of {x} and {y} is {z}")


#Substraction module
elif choice == 2:
        x = int(input("Enter number 1 "))
        y = int(input("Enter number 1 "))
        z = x - y

        print(f"The result of {x} minus {y} is {z}")

#Multiplication module
elif choice == 3:
        x = int(input("Enter number 1 "))
        y = int(input("Enter number 1 "))
        z = x * y

        print(f"The result of {x} multiplied by {y} is {z}")

#Division Module
elif choice == 4:
        x = int(input("Enter number 1 "))
        y = int(input("Enter number 1 "))
        z = x / y

        print(f"The result of {x} divided by {y} is {z}")


elif choice == 5:
        x = int(input("Enter number 1 "))
        y = int(input("Enter number 1 "))
        z = x ** y

        print(f"The result of {x} to the power of {y} is {z}")



else:
    print("Please enter any choice")



