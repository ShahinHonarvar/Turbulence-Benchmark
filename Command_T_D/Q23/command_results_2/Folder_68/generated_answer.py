def find_divisors_in_range(n):
    lst = []
    for i in range(3, n + 1, 2):
        if n % i == 0:
            lst.append(i)
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            lst.append(i)
    return lst
