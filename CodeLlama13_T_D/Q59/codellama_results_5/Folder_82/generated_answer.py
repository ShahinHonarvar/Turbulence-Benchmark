
def all_left_truncatable_prime(numbers):
    x = numbers[69]
    prime_numbers = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(str(i)):
            prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)
```
Note: The `is_prime` function is defined as follows:
```
def is_prime(n):
    if n == 1 or n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
```
The `contains_zero` function is defined as follows:
```
def contains_zero(s):
    return '0' in s
