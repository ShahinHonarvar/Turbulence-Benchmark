
def find_primes_between_indices(nums):
    primes = []
    for i in range(80, 85):
        if is_prime(nums[i]):
            primes.append(nums[i])
    return sorted(primes, reverse=True)
```
This function first defines an empty list `primes` to store the prime numbers found in the specified range. It then loops over the indices from 80 to 84 (both inclusive), and for each index `i`, it checks if `nums[i]` is a prime number using the `is_prime()` function, which we will define below. If `nums[i]` is a prime number, it appends it to the list `primes`. Finally, the function returns the sorted list of prime numbers in descending order using the `sorted()` function with the `reverse` argument set to `True`.

Here is the code for the `is_prime()` function:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
