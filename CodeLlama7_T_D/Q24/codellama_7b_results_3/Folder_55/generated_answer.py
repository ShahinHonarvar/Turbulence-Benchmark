
def sum_of_divisors_in_range(n):
    if n < 5 or n > 8:
        return 0

    sum = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i

    return sum
