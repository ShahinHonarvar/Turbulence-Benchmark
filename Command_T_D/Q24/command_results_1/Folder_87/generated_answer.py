def sum_of_divisors_in_range(n):
    if n < 50 or n > 81:
        return 0
    if n % 2 == 0 and n > 1:
        return n // 2
    for i in range(3, int(n ** .5) + 1, 2):
        if n % i == 0:
            return i + n / i
    return n + (n + 1) / 2
