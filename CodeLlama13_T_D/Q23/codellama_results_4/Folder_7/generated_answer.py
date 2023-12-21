
def find_divisors_in_range(n):
    divisors = []
    for i in range(469, 683):
        if n % i == 0 and i >= 469 and i <= 682:
            divisors.append(i)
    return divisors
