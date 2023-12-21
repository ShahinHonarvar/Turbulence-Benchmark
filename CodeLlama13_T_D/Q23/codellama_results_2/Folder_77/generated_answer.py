
def find_divisors_in_range(n):
    divisors = []
    for i in range(111, 508+1):
        if n % i == 0 and i > 1:
            divisors.append(i)
    return divisors
