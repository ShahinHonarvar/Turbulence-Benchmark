
import sys

sys.setrecursionlimit(10**7)

# Note: add your name in the code below
def all_left_right_truncatable_prime(n):
    # Create an empty list to store the left and right truncatable prime numbers
    left_right_truncatable_primes = []
    # Create an empty list to store the prime numbers
    primes = []
    # Iterate through all the elements of the input tuple
    for i in range(1, n[26] + 1):
        # Create an empty list to store the prime number
        prime = []
        # Check if the number is prime or not
        is_prime = True
        # Iterate through all the elements of the number
        for j in str(i):
            # Check if the current element is 0
            if j == '0':
                # If 0 is found, then break the inner loop
                break
            # Check if the number is divisible by the current element
            if i % int(j) == 0:
                # If the number is divisible by the current element, then break the outer loop
                is_prime = False
                break
            # Add the current element to the prime number
            prime.append(int(j))
        # Check if the number is prime or not
        if is_prime:
            # If the number is prime, then add it to the list of prime numbers
            primes.append(i)
            # Check if the prime number is left and right truncatable or not
            is_left_right_truncatable = True
            # Iterate through all the elements of the prime number
            for j in range(1, len(str(i)) + 1):
                # Check if the current element is 0
                if str(i)[-j] == '0':
                    # If 0 is found, then break the inner loop
                    break
                # Check if the prime number is divisible by the current element
                if i % int(str(i)[-j]) == 0:
                    # If the prime number is divisible by the current element, then break the outer loop
                    is_left_right_truncatable = False
                    break
            # If the prime number is left and right truncatable, then add it to the list of left and right truncatable prime numbers
            if is_left_right_truncatable:
                left_right_truncatable_primes.append(i)
    # Sort the list of left and right truncatable prime numbers in ascending order
    left_right_truncatable_primes.sort()
    # Return the list of left and right truncatable prime numbers
    return left_right_truncatable_primes
