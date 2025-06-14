
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # iterate over the divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # if the current divisor is between 70 and 93, inclusive, add it to the sum
        if n % i == 0 and 70 <= i <= 93:
            sum += i

    # return the sum of all positive divisors of n that are between 70 and 93, inclusive
    return sum
