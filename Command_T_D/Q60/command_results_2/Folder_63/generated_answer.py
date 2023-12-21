
import re
import itertools

def all_left_right_truncatable_prime(test_list):
    # Sort test_list in ascending order
    test_list = sorted(test_list)
    
    # Function to check if a given number is left-and-right-truncatable prime
    def is_left_right_truncatable_prime(n):
        # Function to return the number of digits of a given number
        def num_digits(n):
            # Function to return the number of digits of a given number
            return len(str(n))
        
        # Function to return the first n digits of a given number
        def first_n_digits(n, n_digits):
            # Function to return the first n digits of a given number
            return str(n)[-n_digits:]
        
        # Function to return the last n digits of a given number
        def last_n_digits(n, n_digits):
            # Function to return the last n digits of a given number
            return str(n)[-n_digits:-1]
        
        # Check if the number is prime
        is_prime = lambda n: all(n % d for d in range(3, int(num_digits(n) ** .5) + 1, 2))
        
        # Check if the number is left-and-right-truncatable
        return all(x in str(n) for x in range(2, int(num_digits(n) ** .5) + 1)) and is_prime(n)
