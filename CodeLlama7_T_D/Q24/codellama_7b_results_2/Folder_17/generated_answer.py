
def sum_of_divisors_in_range(n):
    if n < 10 or n > 69:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

            if i * i < n and n % (i * i) == 0:

                divisors.append(i * i)

    sum = 0

    for d in divisors:

        if 10 <= d <= 69:

            sum += d


    return sum
