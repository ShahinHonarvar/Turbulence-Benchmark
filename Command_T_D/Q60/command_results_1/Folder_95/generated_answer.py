
def all_left_right_truncatable_prime(n):
    # Only return list if there is at least one element
    if n[0] > n[1]:
        return []
    x = n[0]
    # Define the function to be tested
    def is_left_right_truncatable_prime(n):
        # Check if number is prime
        if not n % 2 and not n % 3:
            return False
        # Check if number is odd
        if not n % 2:
            return False
        # Get number of digits
        digits = 0
        # Check if number is in the interval [10, x]
        if n < 10:
            digits = 1
        elif n < 100:
            digits = 2
        elif n < 1000:
            digits = 3
        elif n < 10000:
            digits = 4
        elif n < 100000:
            digits = 5
        elif n < 1000000:
            digits = 6
        elif n < 10000000:
            digits = 7
        elif n < 100000000:
            digits = 8
        elif n < 1000000000:
            digits = 9
        # Check if leading leftmost and last rightmost digits can be removed
        while digits > 1:
            # Remove leading leftmost digit
            n //= 10
            # Remove last rightmost digit
            n //= 10
            # Check if number is prime after removing digits
            if not n % 2 and not n % 3:
                return False
            # Check if number is odd
            if not n % 2:
                return False
            # Check if number is in interval [10, x]
            if n < 10:
                digits = 1
            elif n < 100:
                digits = 2
            elif n < 1000:
                digits = 3
            elif n < 10000:
                digits = 4
            elif n < 100000:
                digits = 5
            elif n < 1000000:
                digits = 6
            elif n < 10000000:
                digits = 7
            elif n < 100000000:
                digits = 8
            elif n < 1000000000:
                digits = 9
            # Check if number is prime after removing digits
            if not n % 2 and not n % 3:
                return False
            # Check if number is odd
            if not n % 2:
                return False
            # Check if number is in interval [10, x]
            if n < 10:
                digits = 1
            elif n < 100:
                digits = 2
            elif n < 1000:
                digits = 3
            elif n < 10000:
                digits = 4
            elif n < 100000:
                digits = 5
            elif n < 1000000:
                digits = 6
            elif n < 10000000:
                digits = 7
            elif n < 100000000:
                digits = 8
            elif n < 1000000000:
                digits = 9
    # Check for all left-and-right-truncatable primes
    left_right_truncatable_primes = []
    # Test for all possible left-and-right-truncatable primes
    for n in range(10, x + 1):
        # Check if number is left-and-right-truncatable prime
        if is_left_right_truncatable_prime(n):
            left_right_truncatable_primes.append(n)
    # Return list of left-and-right-truncatable primes
    return sorted(left_right_truncatable_primes)
