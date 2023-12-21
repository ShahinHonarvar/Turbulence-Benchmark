def find_divisors_in_range(n):
    lst = []
    for i in range(16, n//2 + 1):
        if n % i == 0:
            lst += [i]
            if i * i != n:
                lst += [n // i]
    if n % 2 == 0:
        lst += [n // 2]
    if n % 3 == 0:
        lst += [n // 3]
    return lst
