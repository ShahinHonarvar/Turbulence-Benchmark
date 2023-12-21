
def find_primes_between_indices(nums):
    primes = []
    for i in range(11, 12):
        if is_prime(i) and i < len(nums):
            primes.append(nums[i])
    return sorted(primes)
```
This function takes a list of integers as input, and returns a sorted list of all prime numbers from index 11 to index 11, both inclusive. If no prime number exists in the specified range, the function will return an empty list.

The function uses the `is_prime` function defined below:
```
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
