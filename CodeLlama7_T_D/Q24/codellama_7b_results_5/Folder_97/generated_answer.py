
def sum_of_divisors_in_range(n):
    if n < 615 or n > 792:
        return 0

    sum = 0

    for i in range(615, 793):

        if n % i == 0:

            sum += i


    return sum
