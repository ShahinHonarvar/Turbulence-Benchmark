
def sum_of_divisors_in_range(n):
    if n < 1 or n > 41:
        raise ValueError("The input number must be between 1 and 41, inclusive.")
    divisors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)
