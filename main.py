def is_one_digit(v):
    return True if -10 < v < 10 and (v % 1 == 0) else False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and v3 in ["+", "-", "*"]:
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
memory = 0
while True:
    x, oper, y = input(msg_0).split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    if not str(x).replace('.', '').isdigit() or not str(y).replace('.', '').isdigit():
        print(msg_1)
        continue
    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    check(float(x), float(y), oper)
    if oper == '+':
        result = float(x) + float(y)
    elif oper == '-':
        result = float(x) - float(y)
    elif oper == '*':
        result = float(x) * float(y)
    elif oper == '/':
        if float(y) == 0:
            print(msg_3)
            continue
        result = float(x) / float(y)
    print(result)
    while True:
        answer = input(msg_4)
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    answer_temp = input(eval(f"msg_{msg_index}"))
                    if answer_temp == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer_temp == 'n':
                        break
                    else:
                        continue
            else:
                memory = result
        elif answer != 'n':
            continue
        break
    while True:
        answer = input(msg_5)
        if answer != 'y' and answer != 'n':
            continue
        break
    if answer == 'y':
        continue
    break
