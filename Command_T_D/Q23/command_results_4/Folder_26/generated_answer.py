def find_divisors_in_range(n):
    if n < 83 or n > 95:
        return []
    return [i for i in range(1, int(n ** .5) + 1) if n % i == 0]
