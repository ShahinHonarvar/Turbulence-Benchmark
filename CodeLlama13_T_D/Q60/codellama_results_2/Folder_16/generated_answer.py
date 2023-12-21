
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(10, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            primes.append(i)
    
    left_right_truncatable_primes = []
    for prime in primes:
        if is_left_and_right_truncatable_prime(prime):
            left_right_truncatable_primes.append(prime)
    
    return sorted(left_right_truncatable_primes)
```
This function uses the `is_prime` and `contains_zero` functions defined earlier to determine if a number is prime and does not contain 0, respectively. It then checks if each prime number in the list of primes is left-and-right truncatable by using the `is_left_and_right_truncatable_prime` function. If a prime number is left-and-right truncatable, it is added to the list of left-and-right truncatable primes and returned in sorted order.

Here are the definitions of the auxiliary functions:
```
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
```
This function checks if a number `n` is prime by checking if it is divisible by any number between 2 and its square root. If no such number exists, the number is prime.

```
def contains_zero(s):
    return '0' in s
```
This function checks if a string `s` contains the digit '0'.

```
def is_left_and_right_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])) or not is_prime(int(str(n)[i:])):
            return False
    
    return True
