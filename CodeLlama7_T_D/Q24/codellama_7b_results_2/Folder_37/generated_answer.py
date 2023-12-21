
def sum_of_divisors_in_range(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    divisors = []

    for i in range(3, 8):

        if n % i == 0:

            divisors.append(i)

    return sum(divisors) if divisors else 0
