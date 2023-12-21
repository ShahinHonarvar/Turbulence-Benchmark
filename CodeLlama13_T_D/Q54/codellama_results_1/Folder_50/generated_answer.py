
def all_right_truncatable_prime(x):
    prime_list = []
    for i in range(10**5, x+1):
        if is_prime(i) and is_right_truncatable(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)
```
The `is_prime` function checks whether a given number is prime or not by checking for divisibility by all the numbers less than it. The `is_right_truncatable` function checks whether a given number is right-truncatable by removing the last digit and seeing if the result is still a prime number.
```
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_right_truncatable(n):
    while len(str(n)) > 1:
        n //= 10
        if not is_prime(n): return False
    return True
