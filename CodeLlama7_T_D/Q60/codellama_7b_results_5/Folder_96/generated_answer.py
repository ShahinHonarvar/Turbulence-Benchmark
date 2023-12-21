
def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x + 1):
        if is_prime(i) and is_left_right_truncatable_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:

            return False

    return True

def is_left_right_truncatable_prime(n):

    # Check if the number is a prime number
    if not is_prime(n):

        return False

    # Check if the number contains no 0
    for i in range(len(str(n)) - 1, -1, -1):

        if str(n)[i] == '0':

            return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(len(str(n)) - 1, -1, -1):

        for j in range(i + 1, len(str(n)))):

            if str(n)[i] == str(n)[j]:

                return True

    return False
