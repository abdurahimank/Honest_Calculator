while True:
    print("Enter an equation")
    calc = input()
    x, oper, y = calc.split()
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['+', '-', '*', '/']
    if x[0] not in numbers or y[0] not in numbers:
        print("Do you even know what numbers are? Stay focused!")
        continue
    if oper not in operators:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    else:
        break
