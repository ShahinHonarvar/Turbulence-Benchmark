
def find_divisors_in_range(n):
    divisors = []
    for i in range(228, 847):
        if n % i == 0 and i <= 846:
            divisors.append(i)
    return divisors
