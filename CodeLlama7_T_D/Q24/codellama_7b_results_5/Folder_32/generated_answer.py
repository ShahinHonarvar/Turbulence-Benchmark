
def sum_of_divisors_in_range(n):
    if n < 71 or n > 81:
        return 0

    divisors = []

    for i in range(71, 82):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)
