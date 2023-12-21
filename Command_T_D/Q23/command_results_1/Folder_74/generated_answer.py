def find_divisors_in_range(n):
    d = []
    for i in range(40, 75):
        if n % i == 0:
            d.append(i)
            if n != i * i:
                d.append(n // i)
    return d
