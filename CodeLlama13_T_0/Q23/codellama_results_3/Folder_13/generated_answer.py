
def find_divisors_in_range(n):
    divisors = []
    for i in range(472, 828):
        if n % i == 0 and i >= 472 and i <= 827:
            divisors.append(i)
    return divisors
