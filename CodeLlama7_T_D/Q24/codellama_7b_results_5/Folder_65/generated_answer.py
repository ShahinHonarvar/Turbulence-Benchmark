
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # loop through all divisors of n in the range [46, 65]
    for i in range(46, 66):
        if n % i == 0:
            sum += i

    # return the sum
    return sum
