
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_list.append(i)
    # filter the list to only include left-and-right-truncatable prime numbers
    result = []
    for num in prime_list:
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):

    # check if n is a perfect square

    root = int(n ** 0.5)

    if root * root == n:

        return True


    # check if n is divisible by any number between 2 and the square root of n

    for i in range(2, root + 1):

        if n % i == 0:

            return False


    return True


def is_left_right_truncatable_prime(n):

    # check if the number contains any zeros

    if '0' in str(n):

        return False


    # check if the number is prime

    if not is_prime(n):

        return False


    # check if the number remains prime when the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime

    for i in range(len(str(n)) - 1):

        num = int(str(n)[:i] + str(n)[i + 1:]))

        if not is_prime(num):

            return False


    return True
