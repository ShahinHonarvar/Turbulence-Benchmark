
def all_left_truncatable_prime(x):
    x = int(x)
    prime_numbers = []
    
    for i in range(10, x):
        if is_prime(i) and not '0' in str(i):
            prime_numbers.append(i)
            
    left_truncatable_primes = []
    
    for i in prime_numbers:
        truncated_number = int(str(i)[1:])
        
        while truncated_number > 0 and is_prime(truncated_number):
            left_truncatable_primes.append(truncated_number)
            truncated_number //= 10
            
    return sorted(left_truncatable_primes, reverse=True)
```
Note: The `is_prime` function is not defined in this solution, you can define it as follows:
```
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True
