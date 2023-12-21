
def all_left_truncatable_prime(numbers):
    x = numbers[25]
    left_truncatable_primes = []
    for i in range(x):
        if is_prime(i) and not '0' in str(i):
            left_truncatable_primes.append(i)
    
    return sorted(left_truncatable_primes, reverse=True)
```
This function uses a list comprehension to generate all left-truncatable prime numbers less than `x`, and then sorts the list in descending order using the `sorted()` function with the `reverse` parameter set to `True`. The `is_prime()` function is not included in this solution, but it could be implemented as follows:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
