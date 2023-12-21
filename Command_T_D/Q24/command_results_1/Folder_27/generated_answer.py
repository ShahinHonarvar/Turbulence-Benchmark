def sum_of_divisors_in_range(n):
    for i in range(15, 20):
        if n % i == 0:
            continue
        elif i != n // i:
            continue
        else:
            return i + n // i
