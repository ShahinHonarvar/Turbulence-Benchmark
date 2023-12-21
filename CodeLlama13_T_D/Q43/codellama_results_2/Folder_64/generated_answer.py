
def find_primes_between_indices(nums):
    primes = []
    for i in range(7, 10):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
```
Note: The `is_prime` function can be defined as follows:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
