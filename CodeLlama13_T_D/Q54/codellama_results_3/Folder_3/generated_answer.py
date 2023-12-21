
def all_right_truncatable_prime(numbers):
    x = numbers[100]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i) and is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
```
This function takes a tuple of positive integers as an argument, extracts the integer at index 100, and then generates all right-truncatable prime numbers less than that value using the `is_prime` and `is_right_truncatable_prime` functions. The resulting list is sorted in ascending order and returned. If there are no such right-truncatable prime numbers, an empty list is returned.

The `is_prime` function returns `True` if the input integer is a prime number, and `False` otherwise. It uses a simple trial division algorithm to test for divisibility by all integers up to the square root of the input number:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
```
The `is_right_truncatable_prime` function takes an integer as input and returns `True` if it is a right-truncatable prime, and `False` otherwise. It uses the `is_prime` function to test for primality after successively removing the last digit of the input number:
```
def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True
