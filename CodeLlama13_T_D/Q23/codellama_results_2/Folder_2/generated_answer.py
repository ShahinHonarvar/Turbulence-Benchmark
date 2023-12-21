
def find_divisors_in_range(n):
    divisors = []
    for i in range(315, 956):
        if n % i == 0 and i > 314:
            divisors.append(i)
    return divisors
