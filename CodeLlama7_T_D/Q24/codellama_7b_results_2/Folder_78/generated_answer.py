
def sum_of_divisors_in_range(n):
    if n < 20 or n > 50:
        return 0

    divisors = []

    for i in range(20, 51):

        if n % i == 0:

            divisors.append(i)

    return sum(divisors)
