
import itertools

def all_left_right_truncatable_prime(T):
    x = T[86]
    # Create list of all left-and-right-truncatable prime numbers less than or equal to x.
    # This list is initially empty.
    L = []
    # Create a list of all prime numbers less than or equal to x.
    # This list is initially empty.
    # Note that the range [2, x] includes the endpoints, 2 and x.
    for num in range(2, x + 1):
        # Create a copy of the current prime number.
        # This number is initially 2.
        # Note that the number is initially prime because we start with 2.
        copy = num
        # Create a list of prime numbers.
        # This list is initially empty.
        # Note that the list of primes is initially empty.
        primes = []
        # Create a list of all prime numbers less than or equal to x.
        # This list is initially empty.
        # Note that the list of primes is initially empty.
        # This loop iterates over all prime numbers less than or equal to x.
        # Note that the number is initially 2.
        # Note that we are initially iterating over all prime numbers less than or equal to x.
        for p in range(num, x + 1):
            # Check if the current prime number is left-and-right-truncatable.
            # If the current prime number is left-and-right-truncatable, then we add it to the list of left-and-right-truncatable prime numbers.
            # If the current prime number is not left-and-right-truncatable, then we add it to the list of primes.
            # We only need to check the last digit because all left-and-right-truncatable prime numbers contain no 0.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The last digit is always the last digit because we are iterating over all prime numbers less than or equal to x.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The number is initially 2.
            # The number is initially prime because we start with 2.
            # Check if the current prime number is left-and-right-truncatable.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The number is initially 2.
            # The number is initially prime because we start with 2.
            # Check if the current prime number is left-and-right-truncatable.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The number is initially 2.
            # The number is initially prime because we start with 2.
            # Check if the current prime number is left-and-right-truncatable.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The number is initially 2.
            # The number is initially prime because we start with 2.
            # Check if the current prime number is left-and-right-truncatable.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # The number is initially 2.
            # The number is initially prime because we start with 2.
            # Check if the current prime number is left-and-right-truncatable.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
            # We can remove all digits after the last digit because all left-and-right-truncatable prime numbers remain prime if the leading leftmost and
	