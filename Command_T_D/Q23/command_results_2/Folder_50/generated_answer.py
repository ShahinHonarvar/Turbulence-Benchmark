def find_divisors_in_range(n):
    d = []
    for i in range(57, 86):
        if n % i == 0:
            d += [[i]]
            d += [int(n // i)]
    return d
