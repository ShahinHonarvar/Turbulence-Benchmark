def find_divisors_in_range(n):
    lst = []
    for i in range(32, n.bit_length() + 1):
        if n & (1 << i) == 0:
            lst.append(1 << i)
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0:
            lst += [i, n // i]
    if n % 2 == 0:
        lst += [2]
    if n % 3 == 0:
        lst += [3]
    if n % 5 == 0:
        lst += [5]
    if n % 7 == 0:
        lst += [7]
    if n % 11 == 0:
        lst += [11]
    if n % 13 == 0:
        lst += [13]
    if n % 17 == 0:
        lst += [17]
    if n % 19 == 0:
        lst += [19]
    if n % 23 == 0:
        lst += [23]
    if n % 29 == 0:
        lst += [29]
    if n % 31 == 0:
        lst += [31]
    return sorted(set(lst))
