
def find_primes_between_indices(list):
    prime_numbers = []
    for i in range(25, 63):
        if is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)
```
This code defines a function called `find_primes_between_indices` that takes a list of integers as an argument and returns the sorted list of all prime numbers from index 25 to index 62, both inclusive. The function uses the `is_prime` function defined below to determine if each number in the range is prime or not. If no prime number exists in the specified range, the function returns an empty list.
```
def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
