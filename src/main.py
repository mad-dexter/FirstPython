import re


runcalc = True
previous = 0

def evaluate_user_input():
    global runcalc
    global previous

    if previous == 0:
        exp = input("Enter an expression to evaluate : ")
    else:
        exp = input(str(previous))

    if exp == "quit":
        runcalc = False
        print("GoodBye !!!")
    else:
        exp = re.sub('[A-Za-z," ",\'(){},",|]','',exp)
        if exp == "":
            print("Please try again")
        else:
            if previous == 0:
                result = eval(exp)
            else:
                result = eval(str(previous) + exp)
            previous = result

while runcalc:
    evaluate_user_input()