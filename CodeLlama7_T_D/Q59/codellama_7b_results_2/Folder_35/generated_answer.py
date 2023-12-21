
def all_left_truncatable_prime(x):
    # initialize an empty list to store the results
    result = []

    # loop through all numbers less than x
    for i in range(2, x):

        # check if i is a prime number
        if is_prime(i):

            # check if i contains no 0
            if not '0' in str(i):

                # check if the leading leftmost digit of i is successively removed, then all resulting numbers are prime
                if all(is_prime(j) for j in range(10 ** (len(str(i)) - 1), 10 ** len(str(i))))):
                    # if all the conditions are met, add i to the result list
                    result.append(i)

    # return the sorted list of all left-truncatable prime numbers less than x
    return sorted(result)

# a function to check if a number is prime
def is_prime(n):

    # check if n is greater than 1
    if n > 1:

        # loop through all numbers less than or equal to the square root of n
        for i in range(2, int(n ** 0.5) + 1):

            # check if i divides n
            if n % i == 0:

                # if i divides n, return False
                return False

    # if n is less than or equal to 1, return False
    else:

        return False

    # if none of the above conditions are met, return True
    return True
