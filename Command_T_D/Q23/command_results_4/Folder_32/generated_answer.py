def find_divisors_in_range(n):
    return [d for d in range(1, int(n ** .5) + 1) if n % d == 0 and 71 <= d <= 81]
