
def all_left_right_truncatable_prime(tuple):
    x = tuple[618]
    left_and_right_truncatable_primes = []
    for i in range(x+1):
        if is_prime(i) and not any(str(i).startswith('0') or str(i).endswith('0')):
            left_and_right_truncatable_primes.append(i)
    return sorted(left_and_right_truncatable_primes)
```
Note that this code uses a function `is_prime` to check if a number is prime or not. You can define the `is_prime` function as follows:
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
