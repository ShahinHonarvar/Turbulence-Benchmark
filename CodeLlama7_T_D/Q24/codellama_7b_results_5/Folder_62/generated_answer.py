
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum to 0
    sum = 0

    # iterate over the divisors of n in the specified range
    for i in range(59, 89):
        if n % i == 0:
            sum += i

    # return the sum of the divisors in the specified range
    return sum
