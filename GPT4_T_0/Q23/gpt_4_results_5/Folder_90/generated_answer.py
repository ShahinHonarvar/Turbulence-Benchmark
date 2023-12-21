
def find_divisors_in_range(n):
    divisors = []
    for i in range(451, 974):
        if n % i == 0:
            divisors.append(i)
    return divisors
