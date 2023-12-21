
def sum_of_divisors_in_range(n):
    if n < 38 or n > 65:
        return 0

    divisors = []

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

            if i * i < n:

                divisors.append(n // i)

    return sum(divisors)
