
def find_divisors_in_range(n):
    divisors = []
    for i in range(113, 992):
        if n % i == 0 and i > 1:
            divisors.append(i)
    return divisors
