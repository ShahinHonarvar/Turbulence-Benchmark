def find_divisors_in_range(n):
    lst = []
    for i in range(6, n // 2 + 1):
        if n % i == 0:
            lst.append(i)
    for i in range(n // 2, 1, -1):
        if n % i == 0:
            lst.append(i)
    if n == 1:
        lst.append(1)
    if n == 2:
        lst.append(1)
        lst.append(2)
    if n == 3:
        lst.append(1)
        lst.append(2)
        lst.append(3)
    return lst
