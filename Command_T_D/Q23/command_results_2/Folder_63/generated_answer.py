def find_divisors_in_range(n):
    divisors = []
    for i in range(39, 43):
        if n % i == 0:
            divisors.append(i)
            if n != i * i:
                divisors.append(n // i)
    return divisors
