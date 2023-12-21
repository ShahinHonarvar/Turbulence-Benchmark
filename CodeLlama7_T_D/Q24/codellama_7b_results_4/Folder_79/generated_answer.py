
def sum_of_divisors_in_range(n):
    # check if n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    # initialize the sum of divisors to 0
    sum = 0

    # iterate over all divisors of n in the range [1, 8]
    for i in range(1, 9):
        if n % i == 0:
            sum += i

    return sum
