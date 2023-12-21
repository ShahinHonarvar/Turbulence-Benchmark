def find_divisors_in_range(n):
    lst = []
    for x in range(1, n // 2):
        if n % x == 0:
            lst.append(x)
    if n % 2 == 0:
        lst.append(2)
    return [x for x in lst if 28 <= x <= 81]
