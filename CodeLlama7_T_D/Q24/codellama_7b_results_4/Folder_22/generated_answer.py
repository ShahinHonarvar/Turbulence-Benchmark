
def sum_of_divisors_in_range(n):
    if n < 4 or n > 7:
        return 0

    divisors = []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)
