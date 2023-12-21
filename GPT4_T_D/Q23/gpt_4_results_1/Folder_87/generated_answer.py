
def find_divisors_in_range(n):
    divisors = []
    for i in range(50, 82):
        if n%i == 0:
            divisors.append(i)
    return divisors
