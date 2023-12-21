
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_list.append(i)
    # filter the list to only include left-and-right-truncatable prime numbers
    result = [p for p in prime_list if is_left_right_truncatable_prime(p)]
    return result

def is_left_right_truncatable_prime(n):
    # check if n is a prime number
    if not is_prime(n):
        return False

    # check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime
    for i in range(1, len(str(n)))):
        for j in range(i + 1, len(str(n)))):
            if str(n)[:i] == str(n)[j:] and is_prime(int(str(n)[:i]) * int(str(n)[j:]))):
                return True

    # if we reach this point, then n is not a left-and-right-truncatable prime number
    return False

def is_prime(n):

    # check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:
        return False

    # check if n is a prime number using the Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    # if we reach this point, then n is a prime number
    return True
