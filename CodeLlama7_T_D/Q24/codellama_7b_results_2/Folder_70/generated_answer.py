
def sum_of_divisors_in_range(n):
    if n < 586 or n > 840:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)


    for j in range(int(n ** 0.5), 0, -1):

        if n % j == 0:

            divisors.append(j)


    return sum(divisors)
