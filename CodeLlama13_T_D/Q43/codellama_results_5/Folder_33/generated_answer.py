
def find_primes_between_indices(nums):
    primes = []
    for i in range(289, 381+1):
        if is_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)
```
This code defines a function called `find_primes_between_indices` that takes in a list of integers as an argument and returns the sorted list of all prime numbers from index 289 to index 381, both inclusive. If no prime number exists in the specified range, the function should return an empty list.

The function first defines a variable `primes` which will store the prime numbers found in the range. Then it iterates through the indices from 289 to 381 using a for loop and checks if each index is a prime number using the `is_prime` function, which we'll define next.

If an index is found to be a prime number, it is added to the `primes` list. Finally, the function returns the sorted list of all prime numbers from the range in descending order.

The `is_prime` function is defined as follows:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
