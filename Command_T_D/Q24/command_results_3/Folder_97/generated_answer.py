def sum_of_divisors_in_range(n):
    return (sum(range(2, n)) + sum(range(n, 792, n))) if n in range(615, 792) else 0
