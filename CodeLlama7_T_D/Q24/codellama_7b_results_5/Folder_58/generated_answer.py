
def sum_of_divisors_in_range(n):
    if n < 403 or n > 514:
        return 0

    else:

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)

                if n // i != i:
                    divisors.append(n // i)

        return sum(divisors)
