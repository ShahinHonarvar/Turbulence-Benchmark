
def all_right_truncatable_prime(tuple_of_positive_integers):
    # Initialize a list to store the right-truncatable prime numbers
    right_truncatable_primes = []

    # Iterate over the tuple of positive integers
    for x in tuple_of_positive_integers:
        # Check if x is a right-truncatable prime number
        if is_right_truncatable_prime(x):
            # Add x to the list of right-truncatable prime numbers
            right_truncatable_primes.append(x)

    # Return the sorted list of right-truncatable prime numbers in descending order
    return sorted(right_truncatable_primes, reverse=True)
```
```
def is_right_truncatable_prime(n):
    # Check if n is a prime number
    if not is_prime(n):
        return False

    # Iterate over the digits of n from right to left
    for i in range(len(str(n))-1, 0, -1):
        # Remove the last digit of n and check if it is still a prime number
        if not is_prime(int(str(n)[:i])):
            return False

    # If all digits pass the test, n is a right-truncatable prime number
    return True
```
```
def is_prime(n):
    # Check if n is greater than 1
    if n > 1:
        # Iterate over the range of numbers from 2 to the square root of n
        for i in range(2, int(n**0.5) + 1):
            # If n is divisible by any number in the range, it is not prime
            if n % i == 0:
                return False
        # If n has no factors in the range, it is prime
        return True
    # If n is less than or equal to 1, it is not prime
    return False
