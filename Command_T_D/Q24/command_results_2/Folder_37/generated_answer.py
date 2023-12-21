def sum_of_divisors_in_range(n):
    return sum(div for div in range(3, n + 1, 2) if all(x % y == 0 for x, y in zip(range(1, n // 2 + 1), range(2, int(n ** .5) + 1))))
