
def sum_of_divisors_in_range(n):
    if n < 10 or n > 55:
        return 0

    sum = 0

    for i in range(10, 56):

        if n % i == 0:

            sum += i


    return sum
