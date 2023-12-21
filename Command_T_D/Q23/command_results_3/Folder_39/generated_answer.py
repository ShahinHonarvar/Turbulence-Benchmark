def find_divisors_in_range(x):
    if x <= 10:
        return []
    elif x <= 55:
        return [i for i in range(11, x + 1) if x % i == 0]
    else:
        return []
