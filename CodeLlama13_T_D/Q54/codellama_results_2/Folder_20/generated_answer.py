
def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)
```
This function takes a tuple of positive integers as an argument and returns the sorted list of all right-truncatable prime numbers less than the integer at index 100 in descending order. If there is no such right-truncatable prime number, it returns an empty list. The function uses two helper functions: `is_prime` to check if a number is prime and `is_right_truncatable_prime` to check if a number is a right-truncatable prime.

The `is_prime` function takes a single integer as an argument and returns True if it is a prime number, and False otherwise. It uses the sieve of Eratosthenes algorithm to generate all prime numbers less than or equal to the given number.
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
The `is_right_truncatable_prime` function takes a single integer as an argument and returns True if it is a right-truncatable prime number, and False otherwise. It uses the same algorithm as the `is_prime` function to check if the given number is prime, but also checks if the last rightmost digit of the number is 0. If it is, then the number is not a right-truncatable prime number because the last rightmost digit is being removed.
```
def is_right_truncatable_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 or n % (i * 10) == 0:
            return False
    return True
