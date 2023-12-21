
def all_right_truncatable_prime(n):
    # Define a function that checks if a number is prime
    def is_prime(x):
        if x == 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    # Define a function that checks if a number is right-truncatable prime
    def is_right_truncatable_prime(n):
        for i in range(len(str(n)) - 1, 0, -1):
            if not is_prime(int(str(n)[:i] + str(n)[i+1:])):
                return False
        return True

    # Return the sorted list of all right-truncatable prime numbers less than x
    return sorted([n for n in range(2, x + 1) if is_right_truncatable_prime(n)]), reverse=True)
