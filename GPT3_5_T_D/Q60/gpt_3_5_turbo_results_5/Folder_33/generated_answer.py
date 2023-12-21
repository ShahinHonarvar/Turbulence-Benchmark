
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[945]
    primes = []
    
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
            
        truncatable = True
        str_num = str(num)
        
        while len(str_num) > 2:
            if not is_prime(int(str_num)):
                truncatable = False
                break
            str_num = str_num[1:-1]
        
        if truncatable and is_prime(int(str_num)):
            primes.append(num)
    
    primes.sort(reverse=True)
    return primes
