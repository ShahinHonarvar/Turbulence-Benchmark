
def all_left_right_truncatable_prime(x):
    # create a list of prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        # check if i is a prime number
        if is_prime(i):
            # check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # add i to the list of prime numbers
                prime_list.append(i)
    # sort the list of prime numbers in descending order
    prime_list.sort(reverse=True)
    return prime_list

def is_prime(n):
    # check if n is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be a positive integer")

    # check if n is an exact power of 2

    if (n & (n - 1)) == 0:
        # return False if n is an exact power of 2
        return False

    # check if n has more than one factor

    for i in range(2, int(n ** 0.5) + 1):
        # check if i divides n exactly

        if n % i == 0:
            # return False if n has more than one factor
            return False

    # return True if n is a prime number
    return True

def is_left_right_truncatable_prime(n):
    # check if n is a prime number
    if not is_prime(n):
        # return False if n is not a prime number
        return False

    # check if n contains no 0

    if "0" in str(n):
        # return False if n contains 0
        return False

    # check if n remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime

    for i in range(len(str(n)) - 2, len(str(n)) + 1):
        # check if the substring of length 3 starting at position i is equal to the substring of length 2 starting at position i + 1

        if str(n)[i:i + 3] == str(n)[i + 1:i + 3]:
            # return False if n remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime
            return False

    # return True if n is a left-and-right-truncatable prime number
    return True
