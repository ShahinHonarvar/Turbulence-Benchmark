
def all_right_truncatable_prime(n):
    # create a list of prime numbers less than n
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    # filter the list to only include right-truncatable prime numbers
    filtered_primes = []
    for prime in primes:
        if is_right_truncatable_prime(prime):
            filtered_primes.append(prime)
    return sorted(filtered_primes, reverse=True)

def is_prime(n):

    # check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # check if n is a prime number
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_right_truncatable_prime(n):

    # check if n is an integer greater than 1
    if not (isinstance(n, int) and n > 1):
        return False

    # check if the last rightmost digit of n is 1
    if str(n)[-1] != '1':
        return False

    # check if the number formed by removing the last rightmost digit of n is a prime number
    number = int(str(n)[:-1])
    return is_prime(number)
