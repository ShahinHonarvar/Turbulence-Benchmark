def find_divisors_in_range(n):
    lst = []
    for x in range(451, 973):
        if n % x == 0:
            lst.append(x)
            lst += list(range(n // x, n // x + 1, x))
    return lst
