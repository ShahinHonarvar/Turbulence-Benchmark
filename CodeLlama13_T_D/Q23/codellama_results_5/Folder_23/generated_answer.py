
def find_divisors_in_range(n):
    divisors = []
    for i in range(18, 53):
        if n % i == 0 and i in range(18, 53):
            divisors.append(i)
    return divisors
