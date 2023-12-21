def sum_of_divisors_in_range(n):
    divs = set(range(1, int(n ** .5) + 1))
    return sum(div for div in divs if 32 <= div <= 35)
