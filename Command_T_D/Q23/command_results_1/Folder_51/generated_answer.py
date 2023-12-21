def find_divisors_in_range(n):
    divisors = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    if n % 2 == 0:
        divisors.append(2)
    if n % 3 == 0:
        divisors.append(3)
    if n % 5 == 0:
        divisors.append(5)
    if n % 7 == 0:
        divisors.append(7)
    return divisors
