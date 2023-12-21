def find_divisors_in_range(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    for j in range(1, n // 2 + 1):
        if n // j == 0:
            lst.append(j)
    return lst
