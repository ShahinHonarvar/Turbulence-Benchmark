
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # loop through all divisors of n
    for i in range(1, int(n ** 0.5) + 1):
        # check if i is a divisor of n
        if n % i == 0:
            # add the divisor to the sum
            sum += i

    # return the sum of all divisors in the specified range
    return sum
