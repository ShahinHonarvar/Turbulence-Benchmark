
def all_left_right_truncatable_prime(x):
    # Create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x+1):
        if is_prime(i):
            prime_list.append(i)
    # Filter the list to only include left-and-right-truncatable prime numbers
    truncatable_prime_list = []
    for i in prime_list:
        if is_left_right_truncatable_prime(i):
            truncatable_prime_list.append(i)
    # Sort the list in ascending order
    truncatable_prime_list.sort()
    return truncatable_prime_list

def is_left_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits of n are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(len(str(n))) - 1:
        for j in range(i+1, len(str(n)) - 1):
            if is_prime(int(str(n)[:i] + str(n)[j:])):
                return True

    return False


def is_prime(n):

    # Check if n is an integer greater than 1
    if not isinstance(n, int) or n < 2:
        return False

    # Check if n is a prime number using the Sieve of Eratosthenes algorithm
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True
