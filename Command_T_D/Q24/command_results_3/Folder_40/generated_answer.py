def sum_of_divisors_in_range(x):
    return sum(i for i in range(1, int(x ** .5) + 1) if x % i == 0)
