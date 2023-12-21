def sum_of_divisors_in_range(n):
    # type: (int) -> int
    return sum(div for div in range(1, n) if 39 <= div <= 57)
