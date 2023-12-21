def sum_of_divisors_in_range(n):
    from functools import reduce
    from operator import mul
    from functools import reduce
    from functools import reduce
    from functools import reduce
    if n <= 50:
        return 0
    elif n <= 60:
        return reduce(mul, range(1, n + 1))
    elif n <= 70:
        return reduce(mul, range(1, n + 1))
    elif n <= 80:
        return reduce(mul, range(1, n + 1))
    else:
        return 0
