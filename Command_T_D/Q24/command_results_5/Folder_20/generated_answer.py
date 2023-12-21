def sum_of_divisors_in_range(n):
    l, r = 28, 81
    while l <= r:
        mid = l + r >> 1
        if mid == n or mid == n // 2:
            return n * (n + 1) // 2
        elif mid == n // 2:
            return n * (n + 1)
        elif mid <= n // 2:
            return sum_of_divisors_in_range(mid) + sum_of_divisors_in_range(mid + 1)
        else:
            return 0
    return 0
