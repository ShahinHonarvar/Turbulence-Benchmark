def find_divisors_in_range(n):
    d = {}
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            d[i] = 1
    if n % 2 == 0 and n != 2:
        d[2] = 1
    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            d[i] = 1
    if n % 3 == 0 and n != 3:
        d[3] = 1
    return [x for x in range(2, n // 2 + 1) if d[x]]
