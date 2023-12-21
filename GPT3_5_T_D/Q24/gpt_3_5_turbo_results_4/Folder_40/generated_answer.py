
def sum_of_divisors_in_range(n):
    return sum([x for x in range(1, n + 1) if n % x == 0 and 1 <= x <= 2])
