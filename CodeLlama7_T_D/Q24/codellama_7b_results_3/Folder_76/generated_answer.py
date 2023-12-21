
def sum_of_divisors_in_range(n):
    if n < 744 or n > 885:
        return 0

    else:

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):

            if n % i == 0:

                divisors.append(i)

                if i * n // i != n:

                    divisors.append(i * n // i)

        return sum(divisors)
