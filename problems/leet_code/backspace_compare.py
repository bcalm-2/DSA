def backspaceCompare(s, t):
    stack1 = []
    stack2 = []
    def fun(x, stack):
        for i in x:
            if i == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return stack 
    return fun(s, stack1) == fun(t, stack2)