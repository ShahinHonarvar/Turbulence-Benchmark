
def sum_of_divisors_in_range(n):
    if n < 81 or n > 88:
        return 0

    divisors = []

    for i in range(81, 89):

        if i % n == 0:

            divisors.append(i)

    return sum(divisors)
