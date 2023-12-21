
def sum_of_divisors_in_range(n):
    if n < 70 or n > 72:
        return 0

    divisors = []

    for i in range(70, 73):
        if i % n == 0:
            divisors.append(i)

    return sum(divisors)
