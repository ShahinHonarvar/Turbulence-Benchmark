
def all_left_truncatable_prime(x):
    # List of prime numbers less than x
    primes = []

    # Iterate from 2 to x - 1
    for i in range(2, x):
        # Check if i is a prime number
        if is_prime(i):
            # Add i to the list of prime numbers
            primes.append(i)

    return primes
```
Note that this implementation uses the `is_prime` function to check whether a given number is prime. This function can be defined as follows:
```
def is_prime(n):
    # Check if n is less than or equal to 1
    if n <= 1:
        return False

    # Check if n is divisible by 2 to n - 1
    for i in range(2, n + 1):
        if n % i == 0:
            return False

    return True
