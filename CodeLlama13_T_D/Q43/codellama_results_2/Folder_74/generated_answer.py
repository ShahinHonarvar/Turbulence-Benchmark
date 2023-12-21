
def find_primes_between_indices(numbers):
    primes = []
    for i in range(23, 76):
        if is_prime(numbers[i]):
            primes.append(numbers[i])
    return sorted(primes, reverse=True)
```
Here's a function that takes a list of integers and returns the sorted list of all prime numbers from index 23 to index 75, both inclusive, in descending order. If no prime number exists in the specified range, it returns an empty list.

The `is_prime` function is defined separately, as follows:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
