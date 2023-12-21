
def find_divisors_in_range(n):
    divisors = []
    for i in range(38, 65 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
