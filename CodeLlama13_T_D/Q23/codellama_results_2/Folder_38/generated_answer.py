
def find_divisors_in_range(n):
    divisors = []
    for i in range(16, 69):
        if n % i == 0 and i not in divisors:
            divisors.append(i)
    return divisors
