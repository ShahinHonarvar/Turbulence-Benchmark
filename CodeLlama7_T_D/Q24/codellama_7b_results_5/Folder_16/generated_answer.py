
def sum_of_divisors_in_range(n):
    if n < 228 or n > 846:
        return 0

    divisors = []

    for i in range(228, n + 1):

        if n % i == 0:

            divisors.append(i)

    return sum(divisors)
