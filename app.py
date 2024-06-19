import winsound

def f(x: float) -> float:
    # A math Equation
    pass

def play(F, minLimit: float = -1, maxLimit: float = 1, jumps: float = 0.01, timeMs: int = 100, forward: bool = True) -> None:
    lim = 32_767
    if jumps == 0:
        jumps = 1
    if forward:
        if minLimit > maxLimit:
            minLimit, maxLimit = maxLimit, minLimit
        if jumps < 0:
            jumps = -jumps
    else:
        if minLimit < maxLimit:
            minLimit, maxLimit = maxLimit, minLimit
        if jumps > 0:
            jumps = -jumps

    i = minLimit
    while (forward and i <= maxLimit) or (not forward and i >= maxLimit):
        y = int(F(i) * 1000 + 2000)
        if y > lim:
            y = lim
        elif y < 37:
            y = 37
        winsound.Beep(y, timeMs)
        i += jumps
