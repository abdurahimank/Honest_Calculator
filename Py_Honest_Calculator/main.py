def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + " ... lazy"
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + " ... very lazy"
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
        print(msg)


def is_one_digit(v):
    if (v > -10) and (v < 10) and float(v) % 1 == 0:
        return True
    return False


memory = "0"
while True:
    print("Enter an equation")
    calc = input()
    x, oper, y = calc.split()
    x_type = x.replace('.', '').isdigit()
    y_type = y.replace('.', '').isdigit()
    operators = ['+', '-', '*', '/']
    if x == "M":
        x = memory
        x_type = True
    if y == "M":
        y = memory
        y_type = True
    if x_type is False or y_type is False:
        print("Do you even know what numbers are? Stay focused!")
        continue
    if oper not in operators:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    else:
        x = float(x)
        y = float(y)
        check(x, y, oper)
        if oper == "+":
            result = (x + y)
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        else:
            if oper == "/" and y != 0:
                result = x / y
            else:
                print("Yeah... division by zero. Smart move...")
                continue
        print(result)
        while True:
            answer = input("Do you want to store the result? (y / n):")
            if answer == "y":
                if is_one_digit(result):
                    msg = {"msg_10": "Are you sure? It is only one digit! (y / n)",
                           "msg_11": "Don't be silly! It's just one number! Add to the memory? (y / n)",
                           "msg_12": "Last chance! Do you really want to embarrass yourself? (y / n)"}
                    msg_index = 10
                    while True:
                        answer = input(msg["msg_" + str(msg_index)])
                        if answer == "y":
                            if msg_index < 12:
                                msg_index += 1
                            else:
                                memory = result
                                break
                        elif answer == "n":
                            break
                        else:
                            continue
                    break
                else:
                    memory = result
                    break
            elif answer == "n":
                break
            else:
                continue
        while True:
            answer = input("Do you want to continue calculations? (y / n):")
            if answer != "y" and answer != "n":
                continue
            else:
                break
        if answer == "y":
            continue
        else:
            break
