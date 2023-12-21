
def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[23]
    right_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and all(is_prime(i // 10 ** j) for j in range(len(str(i)) - 1)):
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)
```
This code defines a function `all_right_truncatable_prime` that takes a tuple of positive integers as input and returns the sorted list of all right-truncatable prime numbers less than the integer at index 23 in the input tuple. The function uses the `is_prime` function defined below to check if a number is prime, and the `all` function to check if all the numbers are prime when the last digit is successively removed.
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
