
def sum_of_divisors_in_range(n):
    if n <= 43 or n >= 46:
        return 0

    else:

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)

                if i * n >= 43 and i * n <= 46:
                    return sum(divisors)
