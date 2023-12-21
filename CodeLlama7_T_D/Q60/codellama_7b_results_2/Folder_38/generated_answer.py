 def all_left_right_truncatable_prime(x):
    # initialize an empty list to store the results
    result = []
    for i in range(2, x + 1):
        # check if i is a prime number
        if is_prime(i):
            # check if i is left-and-right-truncatable prime number
            if is_left_right_truncatable_prime(i):
                # add i to the result list
                result.append(i)
    # sort the result list in ascending order
    result.sort()
    # return the result list
    return result

def is_prime(n):
    # check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # check if n is divisible by any integer between 2 and the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # if n is greater than 1 and it is not divisible by any integer between 2 and the square root of n, it is prime
    return True

def is_left_right_truncatable_prime(n):
    # check if n is a prime number
    if not is_prime(n):
        return False

    # check if n contains any 0 digits
    if '0' in str(n):
        return False

    # check if the leading leftmost and last rightmost digits of n are both prime numbers
    if not is_prime(int(str(n)[:1])) or not is_prime(int(str(n)[-1:])):
        return False

    # if n is a prime number that contains no 0 digits and the leading leftmost and last rightmost digits of n are both prime numbers, it is a left-and-right-truncatable prime number
    return True
