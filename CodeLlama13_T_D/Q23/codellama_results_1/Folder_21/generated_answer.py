
def find_divisors_in_range(n):
    divisors = []
    for i in range(120, 350):
        if n % i == 0 and i >= 120 and i <= 349:
            divisors.append(i)
    return divisors
