
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[78]
    truncatable_primes = []
    
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        
        truncatable = True
        left = num
        right = num
        
        while left > 10:
            left = int(str(left)[1:])
            if not is_prime(left):
                truncatable = False
                break
        
        while right > 10:
            right = int(str(right)[:-1])
            if not is_prime(right):
                truncatable = False
                break
        
        if truncatable:
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
