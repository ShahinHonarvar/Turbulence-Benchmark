
def all_left_truncatable_prime(nums):
    x = nums[37]
    left_truncatable_primes = []
    for i in range(x, 2, -1):
        if is_prime(i) and not contains_zero(str(i)):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)
```
You can also use the `is_prime` function from the previous question:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
