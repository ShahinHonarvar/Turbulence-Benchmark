
def find_divisors_in_range(n):
    divisors = []
    for i in range(36, 94):
        if n % i == 0 and i > 36:
            divisors.append(i)
    return divisors
