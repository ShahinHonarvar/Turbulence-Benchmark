
def sum_of_divisors_in_range(n):
    if n < 6 or n > 7:
        return 0

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)

            if i * i == n:
                break


    return sum(divisors)
