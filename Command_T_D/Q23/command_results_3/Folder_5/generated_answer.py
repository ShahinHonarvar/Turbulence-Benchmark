def find_divisors_in_range(n):
    divisors = []
    for i in range(7, n // 2):
        if n % i == 0:
            divisors += [[i]]
            if n // i != i:
                divisors += [[n // i]]
    if n % 2 == 0:
        divisors += [[2]]
    if n % 3 == 0:
        divisors += [[3]]
    if n % 5 == 0:
        divisors += [[5]]
    if n % 6 == 0:
        divisors += [[6]]
    return divisors
