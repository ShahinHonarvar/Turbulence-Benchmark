
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    return sorted(primes)
```
This function first checks whether the input number `x` is a prime number using the `is_prime()` function, and then it checks if the number contains any zeroes using the `contains_zero()` function. If both of these conditions are satisfied, the number is added to a list called `primes`. Finally, the function returns the sorted list of all left-and-right-truncatable prime numbers less than or equal to `x`.

Here is the implementation of the `is_prime()` and `contains_zero()` functions:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
