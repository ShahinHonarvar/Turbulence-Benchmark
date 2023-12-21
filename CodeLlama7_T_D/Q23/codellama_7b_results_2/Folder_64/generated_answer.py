
def find_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize an empty list to store the divisors
    divisors = []

    # iterate from 1 to n
    for i in range(1, n + 1):

        # check if i is a divisor of n
        if n % i == 0:

            # add i to the list of divisors
            divisors.append(i)

    # return the list of divisors
    return divisors
