
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum of divisors to 0
    sum_of_divisors = 0

    # loop through all divisors of n between 157 and 902
    for i in range(157, 903):
        if n % i == 0:
            # add the divisor to the sum
            sum_of_divisors += i

    return sum_of_divisors
