
def all_left_truncatable_prime(numbers):
    x = numbers[4]
    prime_list = []
    for i in range(2, x):
        if is_prime(i) and "0" not in str(i):
            prime_list.append(i)
    
    left_truncatable_prime_list = []
    for p in prime_list:
        for i in range(1, len(str(p)) - 1):
            num = int(str(p)[i:])
            if is_prime(num) and "0" not in str(num):
                left_truncatable_prime_list.append(num)
    
    return sorted(left_truncatable_prime_list)
```
Note: The `is_prime` function is used to check if a number is prime or not. It can be defined as follows:
```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
