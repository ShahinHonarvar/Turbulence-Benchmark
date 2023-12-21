
def all_right_truncatable_prime(tuple):
    # initialize an empty list to store the prime numbers
    prime_list = []

    # loop through each element in the tuple
    for i in range(len(tuple)):

        # initialize a variable to store the current element in the tuple
        current_element = tuple[i]

        # check if the current element is a prime number
        if is_prime(current_element):

            # loop through each digit of the current element from right to left
            for j in range(len(str(current_element))) - 1, -1, -1:

                # initialize a variable to store the current digit of the current element
                current_digit = str(current_element)[j]

                # check if the current element is still prime after removing the last rightmost digit
                if is_prime(int(str(current_element)[:j] + str(current_digit)))):

                    # add the current element to the list of prime numbers
                    prime_list.append(current_element)

    # return the sorted list of all right-truncatable prime numbers less than x, or an empty list if there is no such number
    return sorted(prime_list, reverse=True)

def is_prime(n):

    # check if n is a positive integer
    if not (isinstance(n, int) and n > 0):

        # if n is not a positive integer, return False
        return False

    # check if n is equal to 1 or 2
    if n in [1, 2]:

        # if n is equal to 1 or 2, return True
        return True

    # initialize a variable to store the square root of n
    sqrt_n = int(math.sqrt(n))

    # loop through each integer from 2 to the square root of n
    for i in range(2, sqrt_n + 1):

        # check if i is a factor of n
        if n % i == 0:

            # if i is a factor of n, return False
            return False

    # if none of the integers from 2 to the square root of n are factors of n, return True
    return True
