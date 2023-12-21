
def find_divisors_in_range(n):
    # initialize an empty list to store the divisors
    divisors = []

    # loop through all positive integers between 4 and 8 (both inclusive)
    for i in range(4, 9):

        # check if 'i' is a divisor of 'n'
        if n % i == 0:

            # if 'i' is a divisor of 'n', add it to the list of divisors
            divisors.append(i)

    # return the list of divisors (if any)
    return divisors
