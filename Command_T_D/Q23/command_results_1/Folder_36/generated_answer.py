def find_divisors_in_range(n):
    l = []
    for i in range(113, 991 + 1):
        if n % i == 0:
            l.append(i)
            l.append(n // i)
    return l
