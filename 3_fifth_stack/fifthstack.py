stack = []
stat = "ok"

commands = ["+", "-", "*", "/", "PUSH", "POP", "SWAP", "DUP"]
item_commands = ["+", "-", "*", "/", "SWAP"]


def actions(comd, stack=[], val=0):
    global stat
    if len(stack) <= 1 and comd in item_commands:
        stat = "ERROR"
        return

    if comd == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x+y)

    if comd == "-":
        x = stack.pop()
        y = stack.pop()
        stack.append(x-y)

    if comd == "*":
        x = stack.pop()
        y = stack.pop()
        stack.append(x*y)

    if comd == "/":
        x = stack.pop()
        y = stack.pop()
        if y == 0 or y > x:
            stat = "ERROR"
        else:
            stack.append(int(x/y))

    if comd == "PUSH":
        stack.append(val)

    if comd == "POP":
        stack.pop()

    if comd == "SWAP":
        x = stack.pop()
        y = stack.pop()
        stack.append(x)
        stack.append(y)

    if comd == "DUP":
        x = stack.pop()
        stack.append(x)
        stack.append(x)

    if comd == "CLEAR":
        stack.clear()
        stat = "ok"


def executer(act):
    global stat
    stat = "ok"
    if act[0] == "PUSH":
        print("action: {} {}".format(act[0], act[1]))
        actions("PUSH", stack, act[1])
    else:
        print("action: {}".format(act[0]))
        actions(act[0], stack)
    if stat == "ok":
        return stack
    else:
        return stat
