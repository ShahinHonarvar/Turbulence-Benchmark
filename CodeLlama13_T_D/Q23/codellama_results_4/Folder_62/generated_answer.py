
def find_divisors_in_range(num):
    divisors = []
    for i in range(59, 89):
        if num % i == 0 and i > 58:
            divisors.append(i)
    return divisors
