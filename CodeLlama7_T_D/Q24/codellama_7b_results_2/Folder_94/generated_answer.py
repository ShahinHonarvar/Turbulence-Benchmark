
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum of divisors to 0
    sum_divisors = 0

    # loop through the divisors of n between 35 and 37 (both inclusive)
    for i in range(35, 38):
        if n % i == 0:
            # add the current divisor to the sum of divisors
            sum_divisors += i

    # return the sum of all positive divisors of n that are between 35 and 37 (both inclusive)
    return sum_divisors
