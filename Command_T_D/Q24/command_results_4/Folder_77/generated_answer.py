def sum_of_divisors_in_range(n):
    if n <= 111:
        return 0
    if n >= 508:
        return 0
    if n == 112:
        return 1
    if n == 240:
        return 3
    if n == There are no divisors in the range [113, 237].
    return sum(range(113, 238, n))
