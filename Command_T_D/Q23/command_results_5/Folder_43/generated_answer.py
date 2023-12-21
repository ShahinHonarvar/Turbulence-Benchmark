def find_divisors_in_range(n):
    divisors = []
    for i in range(19, 70):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    return divisors
