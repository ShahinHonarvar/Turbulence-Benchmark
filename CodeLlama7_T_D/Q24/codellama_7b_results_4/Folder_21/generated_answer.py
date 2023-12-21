
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # loop through all divisors of n between 120 and 349
    for i in range(120, 350):
        if n % i == 0:
            # add the divisor to the sum
            sum += i

    # return the sum of all positive divisors of n between 120 and 349
    return sum
