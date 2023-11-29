import time as t 
print("Welcome To CALC YOU!")
t.sleep(1)
while True:
    A= eval(input("Enter the first number (a) = "))
    t.sleep(0.5)
    B= eval(input("Enter the second number (b) = "))
    print("Select the opertation you want to perfom. ")
    t.sleep(1)
    print("Press 1 For Addition. ")
    t.sleep(0.5)
    print("Press 2 For Subtraction. ")
    t.sleep(1)
    print("Press 3 For Multiplication. ")
    t.sleep(0.5)
    print("Press 4 For Division.")
    t.sleep(0.5)
    print("Press 5 For b per cent of a.")
    t.sleep(0.5)
    print("Press 6 For a per cent of b.")
    t.sleep(0.5)
    c= int(input("What would you like to perform? \n"))
    if c==1:
        print("Your Answer is", A+B)
    elif c==2:
        print("Your Answer is", A-B)
    elif c==3:
        print("Your Answer is", A*B)
    elif c==4:
        print("Your Answer is", A/B)
    elif c==5:
        d= (A/100)*B
        print("Your answer is", d)
    elif c==6:
        e = (B/100)*A
        print("Your answer is", e)
    else:
        print("Invalid Input")
    t.sleep(1.25)
    D= input("Do you wan to perform any other action? Y/N \n")
    if D=="Y":
        
        pass
    else:
        break
t.sleep(1)
print("Thank For using CALC YOU!")