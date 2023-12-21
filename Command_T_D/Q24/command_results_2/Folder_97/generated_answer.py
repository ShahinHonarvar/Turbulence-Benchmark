def sum_of_divisors_in_range(n):
    if n <= 615 or n >= 792:
        return 0
    else:
        return sum(range(1, int(n ** .5) + 1))
