def sum_of_divisors_in_range(x):
    if x < 5:
        return 0
    elif x > 7:
        return x - 1
    else:
        return x - 1 + sum(range(1, x // 2 + 1))
