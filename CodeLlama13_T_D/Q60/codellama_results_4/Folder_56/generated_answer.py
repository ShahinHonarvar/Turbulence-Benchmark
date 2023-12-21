
def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_left_right_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)

def is_left_right_truncatable_prime(num):
    if str(num).count('0') > 0:
        return False
    
    for i in range(len(str(num))-1, 1, -1):
        left = int(str(num)[:i])
        right = int(str(num)[i:])
        
        if not is_prime(left) or not is_prime(right):
            return False
    
    return True

def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    
    return True
