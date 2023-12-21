def sum_of_divisors_in_range(n):
    divisor_set = set()
    for x in range(16, n // 2 + 1):
        if n % x == 0:
            divisor_set.add(x)
            if x * x != n:
                divisor_set.add(n // x)
    return sum(divisor_set)
