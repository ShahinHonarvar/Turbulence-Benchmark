
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    x = numbers[20]
    truncatable_primes = []
    
    for num in range(x - 1, 0, -1):
        if '0' in str(num):
            continue
        
        is_truncatable = True
        for i in range(1, len(str(num))):
            trunc_num = int(str(num)[i:])
            if not is_prime(trunc_num):
                is_truncatable = False
                break
        
        if is_truncatable and is_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
