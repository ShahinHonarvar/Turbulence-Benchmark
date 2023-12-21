
def all_left_right_truncatable_prime(x):
    # create a list of all prime numbers less than or equal to x
    prime_list = []
    for i in range(2, x + 1):
        if is_prime(i):
            prime_list.append(i)
    # filter the prime list to only include left-and-right-truncatable prime numbers
    left_right_truncatable_prime_list = []
    for i in range(len(prime_list)):
        if is_left_right_truncatable_prime(prime_list[i]):
            left_right_truncatable_prime_list.append(prime_list[i])
    return sorted(left_right_truncatable_prime_list)
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def is_left_right_truncatable_prime(n):
    # check that the number is a prime
    if not is_prime(n):
        return False

    # check that the number contains no 0s
    if "0" in str(n):
        return False

    # check that removing the leading leftmost and last rightmost digits results in a prime number
    for i in range(len(str(n)) - 1):
        if is_prime(int(str(n)[:i] + str(n)[i+1:]))) == False:
            return False

    return True
