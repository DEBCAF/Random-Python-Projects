# Using Iteration
def fIt(num):
    start = 1
    last = 0
    new = 1
    if num != 1:
        for i in range(num-1):
            new = start+last
            last = start
            start = new
    return new

# Using Recursion
def fRe(num):
    if num > 2:
        return fRe(num-2) + fRe(num-1)
    elif num > 1:
        return fRe(num-1) + 0
    else:
        return 1