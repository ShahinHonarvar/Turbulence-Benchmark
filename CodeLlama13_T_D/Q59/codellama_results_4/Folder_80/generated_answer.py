
def all_left_truncatable_prime(x):
    # create an empty list to store the left-truncatable prime numbers
    result = []

    # loop through each number from x down to 10
    for i in range(x, 10, -1):
        # check if the current number is a left-truncatable prime number
        if is_left_truncatable_prime(i):
            # add the number to the result list
            result.append(i)

    return sorted(result, reverse=True)

def is_left_truncatable_prime(n):
    # check if the number contains a 0
    if '0' in str(n):
        return False

    # loop through each digit of the number
    for i in range(1, len(str(n))):
        # remove the leading leftmost digit and check if the resulting number is prime
        if not is_prime(int(str(n)[i:])):
            return False

    return True

def is_prime(n):
    # check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
