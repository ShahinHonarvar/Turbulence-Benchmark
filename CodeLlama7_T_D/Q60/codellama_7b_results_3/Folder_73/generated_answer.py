
def all_left_right_truncatable_prime(x):
    # Initialize an empty list to store the prime numbers
    prime_numbers = []

    # Iterate from 10 to x (inclusive) in steps of 2
    for i in range(10, x+1, 2):

        # Check if the current number is a left-and-right-truncatable prime number
        if is_left_right_truncatable_prime(i):

            # If it is, add it to the list of prime numbers
            prime_numbers.append(i)

    # Return the sorted list of prime numbers
    return sorted(prime_numbers)
```
Here is a function that checks if a given number is a left-and-right-truncatable prime number:

```
def is_left_right_truncatable_prime(n):
    # Check if the current number is prime
    if not is_prime(n):
        return False

    # Check if the leading leftmost and last rightmost digits are simultaneously successively removed down to a one- or two-digit prime.
    for i in range(10, n+1):
        while i % 10 != 1:
            i //= 10

        if is_prime(i):
            return True

    return False
```
Here is a function that checks if a given number is prime:

```
def is_prime(n):

    # Check if the current number is greater than 1
    if n <= 1:
        return False

    # Check if the current number is divisible by any number except for 1 and itself
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True
