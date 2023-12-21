
def all_left_right_truncatable_prime(numbers):
    # Define a helper function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Define a helper function to check if a number is left-and-right-truncatable prime
    def is_lr_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    # X is the integer at index 835 in the tuple
    x = numbers[835]

    # Calculate all left-and-right-truncatable prime numbers less than or equal to x
    lr_primes = [i for i in range(2, x + 1) if is_lr_truncatable_prime(i)]

    # Return sorted list
    return sorted(lr_primes)
