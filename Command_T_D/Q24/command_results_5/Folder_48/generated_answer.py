def sum_of_divisors_in_range(n):
    a = [x for x in range(461, 827+1) if n % x == 0]
    return sum(a)
