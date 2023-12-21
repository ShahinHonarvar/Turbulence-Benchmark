
def find_primes_between_indices(numbers):
    primes = []
    for i in range(287, 928+1):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes)
```
This function takes a list of integers as input and returns the sorted list of all prime numbers from index 287 to index 928, both inclusive. The returned list is in ascending order. If no prime number exists in the specified range, an empty list is returned.

The `is_prime` function is used to check if a given number is prime or not. It takes a single integer as input and returns True if it is prime, False otherwise.
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
