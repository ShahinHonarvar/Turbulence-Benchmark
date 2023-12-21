
def find_divisors_in_range(n):
    divisors = []
    for i in range(50, 81+1):
        if n % i == 0 and i <= 81:
            divisors.append(i)
    return divisors
