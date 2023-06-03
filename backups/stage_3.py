# Project: Honest Calculator
# Stage 3/5: Total recall
msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
memory = "0"
while True:
    x, oper, y = input(msg_0).split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    if x.replace(".", "").isdigit() and y.replace(".", "").isdigit():
        if oper not in ["+", "-", "*", "/"]:
            print(msg_2)
        else:
            if oper == "+":
                result = float(x) + float(y)
            elif oper == "-":
                result = float(x) - float(y)
            elif oper == "*":
                result = float(x) * float(y)
            elif oper == "/" and y != "0":
                result = float(x) + float(y)
            else:
                print(msg_3)
                continue
            print(result)
            while True:
                answer = input(msg_4)
                if answer == "y":
                    memory = str(result)
                    break
                elif answer == "n":
                    break
            while True:
                answer = input(msg_5)
                if answer == "y":
                    to_continue = True
                    break
                elif answer == "n":
                    to_continue = False
                    break
            if not to_continue:
                break
    else:
        print(msg_1)
