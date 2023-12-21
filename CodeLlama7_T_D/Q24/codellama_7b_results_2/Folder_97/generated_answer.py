
def sum_of_divisors_in_range(n):
    if n <= 792 and n >= 615:
        divisors = []

        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n // i)

        return sum(divisors)

    else:

        return 0
