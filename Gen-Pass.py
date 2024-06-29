import string as st
import random
import time as t 
print("*"*40,end = "\n"*2 )
print("      Welcome to the GenPass!",end = "\n"*2)
print("*"*40,end = "\n"*2)
t.sleep(1)
def pass_gen(l):
    t.sleep(1)
    if l <8:
        return "Oops! Too short to become a strong password"
    elif l > 30:
        return "Ahh! Too long to become a good password"
    else:
        pass_list = random.choices(char_string,k = l)
        password = "".join(pass_list)
    return f"Your strong - strong password is: {password}"

char_string = st.ascii_letters + st.digits + "!%&?@$"


while True:
    length = int(input("How long do you want your password to be?\n( It should be in the range of 8 - 30)\n: "))
    print()
    t.sleep(0.2)
    print("Loading",end = "")
    t.sleep(0.3)
    print("..",end = "")
    t.sleep(0.3)
    print(".",end = "\n"*2)
    print(pass_gen(length),end= "\n"*2)
    t.sleep(1.3)
    ask = input("Do you want to go again? Yes/No\n(Wrong input will terminate the program)\n:")
    print("*"*40,end = "\n"*2)
    if ask.lower() == "yes":
        True
    else:
        False
        break
print("Thankyou for using GenPass! (Securing the world)")
print()
print("Be Happy! Visit again 😊")