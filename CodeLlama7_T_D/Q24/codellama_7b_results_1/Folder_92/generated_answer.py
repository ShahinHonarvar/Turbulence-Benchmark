
def sum_of_divisors_in_range(n):
    if n < 8 or n > 9:
        return 0

    else:

        divisors = []

        for i in range(2, int(n ** 0.5) + 1):

            if n % i == 0:

                divisors.append(i)

                if i * i < n and (n // i) != i:

                    divisors.append(n // i)

        return sum(divisors)
