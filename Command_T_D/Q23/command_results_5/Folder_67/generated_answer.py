def find_divisors_in_range(n):
    lst = []
    for i in range(33, n // 2):
        if n % i == 0:
            lst.append(i)
    for i in range(n // 2, 57, 1):
        if n % i == 0:
            lst.append(i)
    return lst
