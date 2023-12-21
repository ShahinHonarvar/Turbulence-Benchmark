
def sum_of_divisors_in_range(n):
    if n <= 0:
        return ValueError("The input number must be a positive integer.")

    divisors = []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:

            divisors.append(i)

    divisors.sort()

    for i in range(len(divisors)):

        if divisors[i] > 8 or divisors[i] < 4:

            del divisors[i]

    return sum(divisors)
