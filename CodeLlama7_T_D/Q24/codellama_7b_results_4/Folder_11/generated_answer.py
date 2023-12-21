
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0

    divisors = []

    for i in range(39, 58):

        if n % i == 0:

            divisors.append(i)

    return sum(divisors)
