def sum_of_divisors_in_range(n):
    # find all divisors of n in range(1, 8)
    divisors = []
    for i in range(1, 8):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    # sum them up
    return sum(divisors)
