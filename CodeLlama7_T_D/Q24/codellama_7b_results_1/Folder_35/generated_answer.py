
def sum_of_divisors_in_range(n):
    if n < 392 or n > 465:
        return 0

    divisors = []

    for i in range(392, n + 1):

        if n % i == 0:

            divisors.append(i)

    return sum(divisors)
