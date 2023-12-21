def find_divisors_in_range(n):
    lst = []
    for x in range(41, n // 2 + 1):
        if n % x == 0:
            lst.append(x)
    for x in range(1, n // 2 + 1):
        if n % x == 0:
            lst.append(x)
    return lst
