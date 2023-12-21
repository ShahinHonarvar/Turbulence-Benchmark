
import itertools

def all_left_right_truncatable_prime(x_range):
    # Check for existence
    if not x_range[94]:
        return []
    # Define the check function
    def check(x):
        # Check for existence
        if x <= x_range[94]:
            # Check for prime
            if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
                # Check for left-and-right-truncatable
                if not str(x).count('0'):
                    return True
        return False
    # Define the generate function
    def generate(x):
        # Generate all left-and-right-truncatable prime numbers less than or equal to x
        yield from itertools.permutations(str(x), 2)
        # Define the range
        for d in range(2, len(str(x)) + 1):
            # Check for existence
            if check(x * 10**(d - 1)):
                # Generate all left-and-right-truncatable prime numbers less than or equal to x
                yield from itertools.permutations(str(x * 10**(d - 1)), 2)
    # Call the generate function
    return sorted(set(generate(x_range[94])))
