def find_divisors_in_range(n):
    if n < 35 or n > 55:
        return []
    lst = []
    for x in range(1, n // 2):
        if n % x == 0:
            lst.append(x)
            lst.append(n // x)
    if n % 2 == 0:
        lst.append(n)
    return lst
