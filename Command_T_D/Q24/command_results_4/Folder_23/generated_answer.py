def sum_of_divisors_in_range(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            if i >= 18 and i <= 52:
                s += i
    return s
