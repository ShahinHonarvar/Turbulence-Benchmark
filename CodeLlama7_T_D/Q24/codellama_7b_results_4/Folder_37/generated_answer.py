
def sum_of_divisors_in_range(n):
    if n < 3 or n > 7:
        return 0

    sum = 0

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            sum += i


            if i * i < n and (n // i) != i:

                sum += n // i


    return sum
