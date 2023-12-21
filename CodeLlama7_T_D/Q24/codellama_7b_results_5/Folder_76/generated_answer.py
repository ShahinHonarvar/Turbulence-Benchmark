
def sum_of_divisors_in_range(n):
    if n < 744 or n > 885:
        return 0

    divisors = []

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)


    for j in range(int(n ** 0.5) + 1, n + 1):

        if n % j == 0:

            divisors.append(j)


    return sum(divisors)
