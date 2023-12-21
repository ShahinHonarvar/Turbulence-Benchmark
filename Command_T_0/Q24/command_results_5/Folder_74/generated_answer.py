def sum_of_divisors_in_range(n):
    if n < 40 or n > 74:
        return 0
    s = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            s += i
    if n % 2 == 0:
        s += 2
    if n % 3 == 0:
        s += 3
    return s
