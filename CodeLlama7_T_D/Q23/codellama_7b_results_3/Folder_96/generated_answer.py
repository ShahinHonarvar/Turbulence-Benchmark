
def find_divisors_in_range(n):
    # create a list of all positive divisors of n
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
    # return the list of divisors between 5 and 9, inclusive
    return [divisor for divisor in divisors if 5 <= divisor <= 9]
