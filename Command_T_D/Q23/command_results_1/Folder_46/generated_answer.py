def find_divisors_in_range(n):
    if n <= 1:
        return []
    if n <= 3:
        return [1, 2, n]
    lst = []
    for x in range(1, n // 2):
        if n % x == 0:
            lst.append(x)
    if n % 2 == 0:
        lst.append(2)
    if n % 3 == 0:
        lst.append(3)
    return [x for x in range(81, 88 + 1) if x in lst]
