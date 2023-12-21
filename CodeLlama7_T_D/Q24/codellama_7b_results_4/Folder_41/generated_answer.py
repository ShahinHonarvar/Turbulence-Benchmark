
def sum_of_divisors_in_range(n):
    if n < 2:
        return 0

    sum = 0

    for i in range(2, min(4, int(n ** 0.5)) + 1):
        if n % i == 0:
            sum += i

    return sum
