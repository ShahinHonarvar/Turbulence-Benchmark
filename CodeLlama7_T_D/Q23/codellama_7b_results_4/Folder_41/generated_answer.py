
def find_divisors_in_range(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors
