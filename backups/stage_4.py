# Project: Honest Calculator
# Stage 4/5: The laziness test
msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):\n"
msg_5 = "Do you want to continue calculations? (y / n):\n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
memory = "0"


def is_one_digit(v):
    if -10 < float(v) < 10 and float(v) % 1 == 0:
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        msg += msg_7
    if (float(v1) == 0 or float(v2) == 0) and v3 in ["+", "-", "*"]:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


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
            check(x, y, oper)
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
