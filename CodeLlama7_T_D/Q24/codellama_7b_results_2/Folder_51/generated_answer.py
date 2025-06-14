
def sum_of_divisors_in_range(n):
    if n <= 1:
        return 0

    divisors = []

    for i in range(2, min(n, 7) + 1):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors)
