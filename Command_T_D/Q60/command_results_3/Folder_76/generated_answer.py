
import itertools

def all_left_right_truncatable_prime(n):
    # Return an empty list if no left-and-right-truncatable prime number exists in the specified range
    if not n:
        return []
    # Define a function to check if a prime number is left-and-right-truncatable
    def is_left_right_truncatable(x):
        # Check if the number is prime
        if not x:
            return True
        # Check if the number contains zero
        if 0 in str(x):
            return False
        # Check if the number remains prime after the leading leftmost and last rightmost digits are removed
        if not str(x)[0] and not str(x)[-1]:
            return True
        if str(x)[0] == '0' and str(x)[-1] == '0':
            return True
        if str(x)[0] == '0':
            return False
        if str(x)[-1] == '0':
            return False
        return True
    # Define a function to return a list of left-and-right-truncatable prime numbers less than or equal to the specified range
    def get_left_right_truncatable_primes(x):
        # Define a list to store the left-and-right-truncatable prime numbers
        left_right_truncatable_primes = []
        # Define a list to store the prime numbers in the specified range
        primes = []
        # Define a list to store the indices of the prime numbers in the specified range
        indices = []
        # Check if the specified range contains at least one prime number
        if x[0] < 2:
            # No prime numbers exist in the specified range
            return left_right_truncatable_primes
        # Get the first prime number in the specified range
        first_prime = next(x[1:], None)
        # Check if the first prime number is left-and-right-truncatable
        if is_left_right_truncatable(first_prime):
            # Add the first prime number to the list of left-and-right-truncatable prime numbers
            left_right_truncatable_primes.append(first_prime)
            # Add the first prime number to the list of prime numbers in the specified range
            primes.append(first_prime)
            # Add the index of the first prime number to the list of indices of prime numbers in the specified range
            indices.append(0)
        # Get the indices of the prime numbers in the specified range
        for i in range(1, len(x)):
            # Check if the current number is prime
            if x[i] > 1:
                # Check if the current number is left-and-right-truncatable
                if is_left_right_truncatable(x[i]):
                    # Add the current prime number to the list of left-and-right-truncatable prime numbers
                    left_right_truncatable_primes.append(x[i])
                    # Add the current prime number to the list of prime numbers in the specified range
                    primes.append(x[i])
                    # Add the index of the current prime number to the list of indices of prime numbers in the specified range
                    indices.append(i)
        # Get the last prime number in the specified range
        last_prime = next(x[:-1], None)
        # Check if the last prime number is left-and-right-truncatable
        if is_left_right_truncatable(last_prime):
            # Add the last prime number to the list of left-and-right-truncatable prime numbers
            left_right_truncatable_primes.append(last_prime)
            # Add the last prime number to the list of prime numbers in the specified range
            primes.append(last_prime)
            # Add the index of the last prime number to the list of indices of prime numbers in the specified range
            indices.append(len(x)-1)
        # Sort the list of indices of prime numbers in the specified range
        indices.sort()
        # Convert the list of indices to a list of left-and-right-truncatable prime numbers
        left_right_truncatable_primes = [primes[i] for i in indices]
        # Sort the list of left-and-right-truncatable prime numbers
        left_right_truncatable_primes.sort()
        return left_right_truncatable_primes
    # Call the function to return a list of left-and-right-truncatable prime numbers less than or equal to the specified range
    return get_left_right_truncatable_primes(n)
