def all_right_truncatable_prime(x):
    lst = []
    for i in range(2, x + 1):
        if all(x % d == 0 for d in range(2, x // 2 + 1)):
            continue
        for d in range(2, x // 2 + 1):
            if x % d == 0:
                continue
            elif x % d == 1:
                lst.append(x // d)
                break
            elif x % d == 2:
                lst.append(x // d)
                break
    return lst
