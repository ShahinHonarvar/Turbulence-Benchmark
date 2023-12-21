
def all_left_truncatable_prime(tuple):
    # initialize variables
    x = tuple[32]
    list = []
    # loop through numbers less than x
    for i in range(1, x):
        # check if number is prime
        if is_prime(i):
            # check if number is left-truncatable prime
            if is_left_truncatable_prime(i):
                # add number to list
                list.append(i)
    return sorted(list)

def is_prime(n):
    # check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # check if n is divisible by 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    # if n is greater than 1 and it is not divisible by 2 to n-1, then it is prime
    return True

def is_left_truncatable_prime(n):
    # check if n contains a leading leftmost digit of 0
    if "0" in str(n):
        return False

    # loop through digits of n in reverse order
    for i in range(len(str(n)))):
        # check if removing the current digit from n results in a prime number
        if is_prime(int(str(n)[1:])):
            # if removing the current digit from n results in a prime number, then return True
            return True

    # if none of the digits of n can be removed without resulting in a non-prime number, then return False
    return False
