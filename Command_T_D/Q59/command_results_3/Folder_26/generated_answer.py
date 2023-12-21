def all_left_truncatable_prime(x):
    # T = ((10**i - 1) for i in range(1, x))
    T = (10**i - 1) for i in range(1, x)
    # S = set(T)
    S = set(T)
    # l = S.copy()
    l = S.copy()
    # S.remove(0)
    S.remove(0)
    # l.remove(0)
    l.remove(0)
    # for e in range(10):
    for e in range(10):
        # for p in range(2, e+1):
        for p in range(2, e+1):
            # if e == 0 or e == 9:
            if e == 0 or e == 9:
                # for i in range(p, x, p):
                for i in range(p, x, p):
                    # if i not in l:
                    if i not in l:
                        # l.add(i)
                        l.add(i)
            else:
                # for i in range(p, x, p):
                for i in range(p, x, p):
                    # if i not in l:
                    if i not in l:
                        # l.add(i)
                        l.add(i)
    # return l
    return l
