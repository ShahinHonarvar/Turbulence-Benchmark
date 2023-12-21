def find_divisors_in_range(n):
    lst = []
    for x in range(4, n + 1):
        if x * x == n:
            lst += [x]
            break
    for x in range(3, n // 2 + 1):
        if n % x == 0:
            lst += [x]
            break
    if n == 1:
        lst += [1, 2, 3, 4, 5, 6]
    return lst
