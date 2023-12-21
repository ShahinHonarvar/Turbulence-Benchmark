
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[803]
    primes = []
    
    for num in range(10, x):
        if '0' in str(num):
            continue
        
        is_left_truncatable = True
        truncated_num = int(str(num)[1:])
        
        while truncated_num > 0:
            if not is_prime(truncated_num):
                is_left_truncatable = False
                break
            truncated_num = int(str(truncated_num)[1:])
        
        if is_left_truncatable:
            primes.append(num)
    
    return sorted(primes)
