
def sum_of_divisors_in_range(n):
    if n < 5 or n > 9:
        return 0

    else:

        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)

        return sum(divisors)
