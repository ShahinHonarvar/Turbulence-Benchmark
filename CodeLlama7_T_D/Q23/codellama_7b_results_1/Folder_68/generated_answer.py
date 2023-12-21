
def find_divisors_in_range(n):
    # create an empty list to store the divisors
    divisors = []

    # loop through all positive integers from 3 to n

    for i in range(3, n + 1):

        # check if i is a divisor of n

        if n % i == 0:

            # if it is, add it to the list of divisors

            divisors.append(i)

    # return the list of divisors that are between 3 and 6, both inclusive

    return divisors
