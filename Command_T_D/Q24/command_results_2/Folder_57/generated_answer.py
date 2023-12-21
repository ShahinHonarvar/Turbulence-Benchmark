def sum_of_divisors_in_range(n):
    if n < 15 or n > 92:
        return 0
    s = 0
    for i in range(15, n//2 + 1):
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
    if n % 2 == 0:
        s += 2
    return s
