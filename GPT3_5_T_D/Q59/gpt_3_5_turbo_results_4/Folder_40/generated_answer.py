
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[10]
    primes = []
    
    for num in range(x-1, 11, -1):
        if '0' not in str(num):
            truncatable = True
            while truncatable and num > 10:
                truncatable = is_prime(num)
                num = int(str(num)[1:])
            
            if truncatable:
                primes.append(num)
    
    return sorted(primes, reverse=True)
