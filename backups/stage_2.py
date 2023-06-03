# Project: Honest Calculator
# Stage 2/5: First calculations
msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
while True:
    x, oper, y = input(msg_0).split()
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
            break
    else:
        print(msg_1)
