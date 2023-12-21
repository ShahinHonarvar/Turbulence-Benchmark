
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[370]
    primes = []
    
    for num in range(x - 1, 0, -1):
        if '0' not in str(num):
            truncatable = True
            truncated_num = num
            
            while truncated_num > 0:
                if not is_prime(truncated_num):
                    truncatable = False
                    break
                truncated_num //= 10
            
            if truncatable:
                primes.append(num)
    
    return sorted(primes, reverse=True)
