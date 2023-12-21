
def all_left_right_truncatable_prime(x):
    # Define a function to check if a number is prime
    def is_prime(n):
        if n == 1 or n % 2 == 0:
            return False

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False

        return True

    # Define a function to check if a number is left-and-right-truncatable prime
    def is_left_right_truncatable_prime(n):
        if not is_prime(n):
            return False

        for i in range(1, int(math.log10(n)) + 1):
            if n % (10 ** i) == 0:
                return False

        return True

    # Generate the list of all left-and-right-truncatable prime numbers less than or equal to x
    prime_numbers = []
    for i in range(2, int(x) + 1):
        if is_left_right_truncatable_prime(i):
            prime_numbers.append(i)

    # Sort the list of prime numbers in descending order and return it
    prime_numbers.sort(reverse=True)
    return prime_numbers
