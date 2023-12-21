def sum_of_divisors_in_range(n):
    # Find the range of divisors.
    d = 1
    while d <= n:
        d += 1
    if d > 846:
        return 0
    d -= 1
    range_start = 228
    range_end = 846
    # Find the sum of divisors.
    sum_ = 0
    for d in range(range_start, range_end + 1):
        if n % d == 0:
            sum_ += d
            if d * (d + 1) / 2 <= n:
                sum_ += d * (d + 1)
    return sum_
