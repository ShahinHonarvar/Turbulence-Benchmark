
def find_divisors_in_range(n):
    divisors = []
    for i in range(224, 584+1):
        if n % i == 0:
            divisors.append(i)
    return divisors
