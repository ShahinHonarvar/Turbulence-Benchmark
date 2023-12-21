
def sum_of_divisors_in_range(n):
    if n < 472 or n > 827:
        return 0
    else:
        return sum(d for d in range(1, n + 1) if n % d == 0 and 472 <= d <= 827)
