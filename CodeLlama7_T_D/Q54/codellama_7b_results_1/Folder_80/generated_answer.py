
def all_right_truncatable_prime(tuple):
    # initialize an empty list to store the prime numbers
    prime_numbers = []

    # loop through the tuple of positive integers
    for i in range(len(tuple)):
        # get the current number being checked
        num = tuple[i]

        # check if the current number is a prime number
        if is_prime(num):
            # store the current prime number in the list
            prime_numbers.append(num)

    # sort the list of prime numbers in descending order
    prime_numbers.sort(reverse=True)

    # return the sorted list of right-truncatable prime numbers less than x, or an empty list if there is no such prime number
    return prime_numbers
