memory = 0
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
