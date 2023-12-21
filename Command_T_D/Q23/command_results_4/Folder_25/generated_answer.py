def find_divisors_in_range(n):
    lst = []
    for i in range(84, 86 + 1):
        if n % i == 0:
            lst.append(i)
            lst += range(n // i, i, i)
    return lst
