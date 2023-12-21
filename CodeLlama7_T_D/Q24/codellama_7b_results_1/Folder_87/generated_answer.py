
def sum_of_divisors_in_range(n):
    if n <= 0:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

            if i * i < n and (i * i - n) % i == 0:

                divisors.append(i * i - n)

    return sum([d for d in divisors if 50 <= d <= 81])
