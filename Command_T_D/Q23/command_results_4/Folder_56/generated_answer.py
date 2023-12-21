def find_divisors_in_range(x):
    lst = []
    for i in range(6, x + 1):
        if i == x or i == x // i:
            continue
        elif x % i == 0:
            lst.append(i)
            lst.append(x // i)
    return lst
