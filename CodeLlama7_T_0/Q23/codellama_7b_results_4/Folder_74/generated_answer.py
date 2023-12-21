
def find_divisors_in_range(n):
    divisors = []
    for i in range(40, 75):
        if n % i == 0:
            divisors.append(i)
    return divisors
