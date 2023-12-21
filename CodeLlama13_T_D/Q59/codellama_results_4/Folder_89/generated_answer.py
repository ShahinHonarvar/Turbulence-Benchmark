
def all_left_truncatable_prime(x):
    primes = []
    for i in range(10**9, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    return sorted(primes, reverse=True)
```
This function uses a naive approach to check for prime numbers by iterating through all the numbers between 10**9 and x+1. It then checks if each number is prime using the `is_prime()` function defined below. If a number is prime, it checks if it contains any zeroes using the `contains_zero()` function defined below. If neither of these conditions are true, the number is added to the list of all left-truncatable prime numbers and sorted in descending order.
```
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contains_zero(s):
    return '0' in s
