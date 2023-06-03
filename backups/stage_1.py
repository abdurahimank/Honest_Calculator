# Project: Honest Calculator
# Stage 1/5: Data collection
msg_0 = "Enter an equation\n"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
while True:
    x, oper, y = input(msg_0).split()
    if x.replace(".", "").isdigit() and y.replace(".", "").isdigit():
        if oper not in ["+", "-", "*", "/"]:
            print(msg_2)
        else:
            break
    else:
        print(msg_1)
