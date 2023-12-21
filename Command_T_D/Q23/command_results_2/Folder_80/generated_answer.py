def find_divisors_in_range(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    if n != 1:
        divisors.append(1)
    for i in range(70, 94):
        if n % i == 0:
            divisors.append(i)
    return divisors
