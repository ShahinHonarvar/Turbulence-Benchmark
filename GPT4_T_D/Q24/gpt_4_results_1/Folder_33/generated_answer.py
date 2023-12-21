
def sum_of_divisors_in_range(n):
    if n < 157:
        return 0

    sum = 0
    for i in range(157, min(n, 902) + 1):
        if n % i == 0:
            sum += i

    return sum
