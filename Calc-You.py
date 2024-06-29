print("*"*25)
print()
print("  Welcome to Calc You!")
print()
print("*"*25)
state = input("Wanna use me? Yes/No (Wrong input will terminate the program): ")
while state.lower() == "yes":
    num1 = eval(input("Enter the first number: "))
    num2 = eval(input("Enter the second number: "))
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    print()
    op = int(input("Enter the serial of the operation you want to perform: "))
    if op == 1:
        print("The addition is %d"%(num1+num2))
    elif op == 2:
        print("The subtraction is %d" % (num1 - num2))
    elif op == 3:
        print("The multiplication is %d"%(num1*num2))
    elif op == 4:
         if num2 == 0:
            print("Error: Division by zero")
         else:
            print("The division is %f" %(num1 / num2))
    else:
        print("Wrong input")
    state = input("You want to try again? Yes/No (Wrong input will terminate the program): ")

print()
print("Thank you for using Calc- You! Bye-Bye")
print()