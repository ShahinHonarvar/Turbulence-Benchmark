def find_divisors_in_range(n):
    divisors = []
    for i in range(48, 62):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return divisors
