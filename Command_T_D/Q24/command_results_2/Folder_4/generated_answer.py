def sum_of_divisors_in_range(n):
    if n < 48 or n > 60:
        return 0
    s = 0
    for i in range(1, int(n ** .5) + 1):
        if n % i == 0:
            j = n / i
            while j <= n:
                s += j
                j *= i
    return s
