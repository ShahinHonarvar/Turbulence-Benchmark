
def sum_of_divisors_in_range(n):
    if n < 33 or n > 57:
        return 0

    sum = 0

    for i in range(33, n + 1):
        if n % i == 0:
            sum += i

    return sum
