def sum_of_divisors_in_range(x):
    if x < 60 or x > 86:
        return 0
    else:
        return sum(range(x, x+1, x))
