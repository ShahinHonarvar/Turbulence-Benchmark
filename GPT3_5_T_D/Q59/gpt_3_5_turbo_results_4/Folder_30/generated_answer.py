
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    num = str(n)
    while len(num) > 1:
        num = num[1:]
        if not is_prime(int(num)):
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[37]
    truncatable_primes = []
    
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
