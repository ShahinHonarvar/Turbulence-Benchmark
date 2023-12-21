def sum_of_divisors_in_range(n):
    if n < 3:
        return 0
    elif n < 6:
        divisors = [x for x in range(3, int(n ** .5) + 1) if n % x == 0]
        if divisors:
            return sum(divisors)
    return 0
