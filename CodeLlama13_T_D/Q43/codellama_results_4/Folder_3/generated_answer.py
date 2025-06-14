
def find_primes_between_indices(nums):
    primes = []
    for i in range(80, 84 + 1):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
```
You can use the following helper function to check if a number is prime:
```
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
