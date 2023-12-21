
def find_divisors_in_range(n):
    divisors = []
    for i in range(58, 91):
        if n % i == 0:
            divisors.append(i)
    return divisors
